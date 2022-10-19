import os, time, urllib, json
import concurrent.futures
import selenium, requests
from selenium import webdriver

exc = concurrent.futures.ThreadPoolExecutor(max_workers=6)
drivers = []

class_name = webdriver.common.by.By.CLASS_NAME
css_selector = webdriver.common.by.By.CSS_SELECTOR
xpath = webdriver.common.by.By.XPATH
driver_path = "misc/msedgedriver"
browsers = dict(
	edge=dict(
		driver=webdriver.edge.webdriver.WebDriver,
		service=webdriver.edge.service.Service,
		options=webdriver.EdgeOptions,
		path=driver_path,
	),
)
browser = browsers["edge"]

def create_driver():
	ts = time.time_ns()
	folder = os.path.join(os.getcwd(), f"d~{ts}")
	service = browser["service"](browser["path"])
	options = browser["options"]()
	options.headless = True
	options.add_argument("--disable-gpu")
	prefs = {"download.default_directory" : folder}
	options.add_experimental_option("prefs", prefs)

	try:
		driver = browser["driver"](
			service=service,
			options=options,
		)
	except selenium.common.SessionNotCreatedException as ex:
		if "Current browser version is " in ex.args[0]:
			v = ex.args[0].split("Current browser version is ", 1)[-1].split(None, 1)[0]
			url = f"https://msedgedriver.azureedge.net/{v}/edgedriver_win64.zip"
			import requests, io, zipfile
			with requests.get(url, headers={"User-Agent": "Mozilla/6.0"}) as resp:
				with zipfile.ZipFile(io.BytesIO(resp.content)) as z:
					with z.open("msedgedriver.exe") as fi:
						with open("misc/msedgedriver.exe", "wb") as fo:
							b = fi.read()
							fo.write(b)
			driver = browser["driver"](
				service=service,
				options=options,
			)
		else:
			raise
	driver.folder = folder
	return driver

def ensure_drivers():
	while len(drivers) < 2:
		drivers.append(exc.submit(create_driver))
		time.sleep(1)
def get_driver():
	if not drivers:
		drivers.append(exc.submit(create_driver))
	try:
		driver = drivers.pop(0)
		if hasattr(driver, "result"):
			driver = driver.result()
	except selenium.common.exceptions.WebDriverException:
		driver = create_driver()
	else:
		try:
			exc.submit(getattr, driver, "title").result(timeout=0.25)
		except:
			from traceback import print_exc
			print_exc()
			driver = create_driver()
	exc.submit(ensure_drivers)
	return driver

def safecomp(gen):
	while True:
		try:
			e = next(gen)
		except StopIteration:
			return
		except selenium.common.StaleElementReferenceException:
			continue
		yield e

def vague(t):
	t = t.casefold().replace("'", "")
	return any(t.startswith(i) for i in ("im unsure", "im not sure", "its ", "it is", "i think it", "i dont know", "i do not know", "i think you", "i am unsure", "i am not sure"))

def literal_question(t):
	t = t.casefold().replace("'", "")
	if t.startswith("whats your") or t.startswith("what is your") or t.startswith("what are your") or t.startswith("what do you"):
		return False
	return any(t.startswith(i) for i in ("whats ", "what ", "wheres ", "where ", "whos ", "who ", "whens ", "when ", "whys ", "why ", "hows ", "how "))

def valid_response(t):
	t = t.strip()
	if t in ("View all", "Feedback", "?", "？", "•", "·"):
		return False
	if t.startswith("Images for "):
		return False
	if t.startswith("Missing: "):
		return False
	if not t:
		return False
	return t

swap = {
	"I": "you",
	"Me": "You",
	"me": "you",
	"You": "I",
	"you": "me",
	"Your": "My",
	"your": "my",
	"My": "Your",
	"my": "your",
}

class Bot:

	def __init__(self, token=""):
		self.token = token
		self.history = {}
		self.timestamp = time.time()

	def ask(self, q):
		driver = get_driver()

		folder = driver.folder
		search = f"https://www.google.com/search?q={urllib.parse.quote_plus(q)}"
		fut = exc.submit(driver.get, search)
		fut.result(timeout=16)

		try:
			elem = driver.find_element(by=webdriver.common.by.By.ID, value="rso")
		except:
			return ""
		res = elem.text
		drivers.append(driver)
		if res.startswith("Calculator result\n"):
			response = " ".join(res.split("\n", 3)[1:3])
		else:
			res = "\n".join(r.strip() for r in res.splitlines() if valid_response(r))
			# print(res)
			fut = exc.submit(
				requests.post,
				"https://api-inference.huggingface.co/models/salti/bert-base-multilingual-cased-finetuned-squad",
				data=json.dumps(dict(
					inputs=dict(
						question=q,
						context=res,
					),
				)),
				headers=dict(cookie=f"token={self.token}"),
			)
			resp = requests.post(
				"https://api-inference.huggingface.co/models/deepset/roberta-base-squad2",
				data=json.dumps(dict(
					inputs=dict(
						question=q,
						context=res,
					),
				)),
				headers=dict(cookie=f"token={self.token}"),
			)
			resp2 = fut.result()
			# print(resp.json(), resp2.json())
			if resp.status_code in range(200, 400):
				a1 = resp.json()
				if resp2.status_code in range(200, 400):
					a2 = resp2.json()
					if a2["score"] > a1["score"] and len(a2["answer"]) > len(a1["answer"]):
						a1 = a2
			else:
				resp2.raise_for_status()
				a1 = resp2.json()
			response = a1["answer"]

		response = response.strip()
		# self.history[q] = response
		return response

	def talk(self, i, recursive=True):
		t = time.time()
		if t > self.timestamp + 720:
			self.history.clear()
		self.timestamp = t
		if not recursive or literal_question(i):
			words = i.split()
			i = " ".join(swap.get(w, w) for w in words)
			response = self.ask(i)
			if response and response.casefold() != i.casefold():
				return response
		self.history.pop(i, None)
		inputs = dict(
			generated_responses=list(self.history.values()),
			past_user_inputs=list(self.history.keys()),
			text=i,
		)
		fut = exc.submit(
			requests.post,
			"https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill",
			data=json.dumps(dict(
				inputs=inputs,
			)),
			headers=dict(cookie=f"token={self.token}"),
		)
		resp = requests.post(
			"https://api-inference.huggingface.co/models/microsoft/DialoGPT-large",
			data=json.dumps(dict(
				inputs=inputs,
			)),
			headers=dict(cookie=f"token={self.token}"),
		)
		resp2 = fut.result()
		if resp.status_code in range(200, 400):
			a1 = resp.json()["generated_text"].strip().replace("  ", " ")
			# print(a1)
			if a1.lower() == i.lower() or vague(a1) or a1.lower() in (a.lower() for a in self.history.values()):
				a1 = ""
			if resp2.status_code in range(200, 400):
				a2 = resp2.json()["generated_text"].strip().replace("  ", " ")
				# print(a2)
				if a2.lower() == i.lower() or vague(a2) or a1.lower() in (a.lower() for a in self.history.values()):
					a2 = ""
				if len(a2) > len(a1) * 2 and (len(a1) < len(i) / 2 or (a1 and not a1.isupper() and a2 and a2.isupper())):
					a1 = a2
		else:
			resp2.raise_for_status()
			a1 = resp2.json()["generated_text"].strip()
			if vague(a1):
				a1 = ""
		response = a1
		if recursive and not response:
			return self.talk(i, recursive=False)
		if not response:
			response = resp.json()["generated_text"].strip().replace("  ", " ") or resp2.json()["generated_text"].strip().replace("  ", " ")
		if not response:
			response = "Sorry, I don't know."
		self.history[i] = response
		return response

if __name__ == "__main__":
	token = "WiqIYppNqlsIPISiLnzffiGdSTliJJDBPJyeFupzRkuwvKPQFjfUTPLyApKbTbUNyWLxIRieUAhekwwESNBCbgJLudYXohddHNMkawjlFLUKTHnyhcvwvFCTmlVIkYcU"
	bot = Bot(token)
	while True:
		print(bot.talk(input()))