import os, time, datetime, traceback

def kill(count=1):
    for i in range(count):
        filt = "taskkill /f /fi \"windowtitle eq " + name + "\""
        os.system(filt)
        filt = "taskkill /f /fi \"windowtitle eq " + opt + name + "\""
        os.system(filt)

def delete(f):
    while f in os.listdir():
        try:
            os.remove(f)
        except:
            print(traceback.format_exc())
            time.sleep(1)
    
name = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
opt = "Select "
op = (
    "start powershell -NoExit -Command \"$OutputEncoding = "
    + "[Console]::OutputEncoding = [Text.UTF8Encoding]::UTF8\"; .\\bot.bat"
    )
#name = "C:\\WINDOWS\\system32\\cmd.exe"
#op = "start cmd /abovenormal /c bot.bat"

sd = "shutdown.json"
hb = "heartbeat.json"

kill(2)
delete(sd)
delete(hb)

while not sd in os.listdir():
    os.system(op)
    print("Bot started.")
    time.sleep(20)
    print("Heartbeat started.")
    alive = True
    while alive:
        f = open(hb, "wb")
        f.close()
        print(
            "Heartbeat at "
            + str(datetime.datetime.now())
            + "."
            )
        time.sleep(2)
        for i in range(3):
            time.sleep(1)
            if hb in os.listdir():
                alive = False
                break
    kill(3)
    print("Bot closed without shutdown signal, restarting...")
    
kill(2)
delete(hb)
delete(sd)
        
print("Shutdown signal confirmed. Press [ENTER] to close.")
input()
