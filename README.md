<h1 align="center">
  <img src="https://raw.githubusercontent.com/thomas-xin/Image-Test/master/title-rainbow.webp">
  <br>
  <a href="https://mizabot.xyz">Miza</a>
</h1>


<h4 align="center">A multipurpose Discord bot created by <a href="https://github.com/thomas-xin">Thomas Xin</a>.</h4> <br>

<p align="center">
<a href="https://github.com/thomas-xin/Miza/network/members">
<img alt="GitHub forks" src="https://img.shields.io/github/forks/thomas-xin/Miza?style=plastic&label=Forks">
</a>

<a href="https://github.com/thomas-xin/Miza/stargazers">
<img alt="GitHub Stars" src="https://img.shields.io/github/stars/thomas-xin/Miza?label=Stars&style=plastic">
</a>

<a href="https://github.com/thomas-xin/Miza/issues">
<img alt="GitHub issues" src="https://img.shields.io/github/issues/thomas-xin/Miza?style=plastic&label=Issues">
</a>

<a href="https://github.com/thomas-xin/Miza/graphs/contributors">
<img alt="GitHub contributors" src="https://img.shields.io/github/contributors/thomas-xin/Miza?style=plastic&label=Contributors">
</a>

<a href="https://github.com/thomas-xin/Miza/blob/master/LICENSE.md">
<img alt="GitHub License" src="https://img.shields.io/github/license/Thomas-Xin/Miza?style=plastic&label=License">
</a>

</p>

<p align="center">
Miza's dedicated creator loves to find ways to make Miza bigger and better all the time, with lots of code, optimization
and fun to be had! with Features Including: <b>Moderation, Music, Fun, Image Manipulation, and more!</b>
</p>

<p align="center">
Please support the development of Miza here if you enjoy her services, or would like access to her premium features!<br>
https://ko-fi.com/mizabot<br>
Miza has been free to use for 3 years now since the start of her development, but is quickly becoming more expensive to sustain. Any donations are greatly appreciated, and 100% will go towards supporting Miza's future!
</p>

<h2 align="center">
Table of Contents
</h2>

Sections     | Explanations
------------ | -------------
[Hosting Miza!](#Hosting-Miza)        | Will talk you through the basics of how to host the code, covering potential error-prone areas!
[Folder Structure](#Folder-Structure) | Will talk you through where everything within the code files can be found!
[Support!](#Support)                  | Links to where you can find Miza and get support!
[Credits](#Credits)                   | Credits to all contributors


<a id="Hosting-Miza"></a>
## Hosting Miza!

#### Prerequisites:

* [Git](https://git-scm.com/downloads)
* [Python](https://www.python.org/downloads/)
* [Discord Bot Token](https://discord.com/developers/) (_Choose your Desired Bot then go to **Bot** and under Token click **Copy**_)

<br>

As of 26 September 2021, Miza now fully works on Windows and Linux. If you're planning to run Miza through a Docker container, there is a working [Dockerfile](https://cdn.discordapp.com/attachments/731709481863479436/891402916265594980/Dockerfile) provided that you may use as a template. Note that if you choose to use this, all other installation steps may be skipped, as said Dockerfile includes all necessary installation preparations.

### Installing Miza

* Launch Git Bash.

* Navigate to your desired directory, by typing this command in Git Bash (or Linux terminal):
```bash
cd [Desired Directory]
Example: cd C:/Users/Miza/Documents/Projects/
```

* If on Linux, the following must be installed (use `yum install` on other distributions of Linux as required):
```bash
sudo apt install git
sudo apt install python3 python3-pip python3-tk
sudo apt install libgmp-dev libmpfr-dev libmpc-dev
```

* Clone this Repository, by typing this command:
```bash
git clone https://github.com/thomas-xin/Miza.git
```

* Run `main.bat` the bot will automatically create an `auth.json` file.

* Edit `auth.json` file (prefix, discord_token, etc)

* Run `main.bat` again.  _(Miza should now start successfully, and be ready for use.  if not read the [next section](#common-issues))_ 

<br>

<a id="common-issues"></a>
### Common Issues & FAQ:

<br>

#### Dependencies:

* Miza should automatically download and install the required dependencies immediately after running her for the first time, notably the Python modules and FFmpeg.

##### Additional Notes:

> _As of 08/12/2021, FFmpeg will be automatically installed after first run, Miza is also going to look through the servers it is in to seek out open candidates for placing some emojis that Miza will also require for certain UI features, so make sure you have a good space set up too. Finally, all API Keys that Miza will require as located in *auth.json* you will have to obtain yourself._

<br>

#### Voice commands not working:

* Make sure you have [FFmpeg](https://www.ffmpeg.org/download.html) and [Python](https://www.python.org/downloads/) installed onto your computer and in your PATH (it doesn't need to be in the same directory as Miza). I uh... Actually have my ffmpeg pathed by pathing to the misc folder found in [Miza Player](https://github.com/thomas-xin/Miza-Player) (an awesome program you should definitely try out!) 🙃

![ffmpeg](https://cdn.discordapp.com/attachments/688253918890688521/777473182294474753/image0.png)

_Note: voice commands run in a subprocess concurrently to the main program. If you are still facing issues, check the [support](#Support) section._

#### MemoryError():

* This used to be an issue caused by Miza trying to cache too much at one time. This caching system has been watered down significantly since the time this README was made, so this wont be as likely of an issue anymore. But in case it is still a problem, here's how to fix it. Head on over to the top of *bot.py*, and look for the following function:

```python
def __init__(self, cache_size=4194304, timeout=24):
        self.start_time = utc()
        super().__init__(max_messages=256, heartbeat_timeout=60, guild_ready_timeout=5, intents=self.intents)
        self.cache_size = cache_size
        self.cache = fcdict({c: {} for c in self.caches})

        # Code continues...
```

Just reduce the number in `cache_size=4194304` and you should be good to go.

_Note: memory cache gets cleared upon reset, and Miza has a separate disk cache that doesn't upon reset, but all files in the caches get automtically cleared after 2 weeks._

####  IP Address exposure:

* Miza used to host a few Minecraft Servers which is why this feature used to be a doxx moment for me. That is no longer a risk, but Miza will still obtain your IP Address to store it internally for features such as the webserver.

#### Where does Miza log?

Miza logs up to three places:
* `log.txt` (which the file gets refreshed upon restart)<sup><a href="#logtxt-image">1</a></sup>
* The Console from which Miza is running.<sup><a href="#consolelog-image">2</a></sup>
* Log within Discord itself (which isn't hardcoded, you can enable it as displayed below) <sup><a href="#discordlog-image">3</a></sup>

_<a id="logtxt-image"><sup><a href="#logtxt-image">[1]</a></sup> Image showing an example of `log.txt` file:</a>_ 

![Screenshot1](https://cdn.discordapp.com/attachments/727087981285998593/777554361769000960/Capture10.PNG)

_<a id="consolelog-image"><sup><a href="#consolelog-image">[2]</a></sup> Image showing an example of a Console running Miza:</a>_ 

![Screenshot2](https://cdn.discordapp.com/attachments/727087981285998593/777554360859099146/Capture9.PNG) 

_<a id="discordlog-image"><sup><a href="#discordlog-image">[3]</a></sup> Image showing How to enable log in Discord:</a>_ 

![Screenshot3](https://cdn.discordapp.com/attachments/688253918890688521/804652403445727272/unknown.png)
![Screenshot4](https://cdn.discordapp.com/attachments/727087981285998593/777554358095183893/Capture8.PNG) 

_Note: execute the command `[prefix]exec -e log` to enable discord logging._

<a id="Folder-Structure"></a>
## Folder Structure

#### Project Directory:

* Has all your generic license, requirements, etc... (Though requirements is necessary for the *install_update* functionality which, automatically checks for and installs any missing modules.) But most significantly, the main files responsible for running the bots code. Throughout the code, you will frequently see `from common import *`, which is because *common.py* contains all the main necessary functions and imports to be used throughout. *main.py* is the main process, while everything else runs as a subprocess, so if you make any changes to main.py, it'll require a manual restart. Most of the bots optimization and data collection functionality can be found in these files, (such as running the bot of course, starting the heartbeat.tmp and other log related code, caching, assigning variables of the GitHub Directory link, default bot prefix, etc...) As for where things are located...

#### Commands:

* You may think its unnecessary to explain all this, but before I learnt my way around, I got so lost in all of Miza's files, so hopefully this is helpful. The commands folder speaks for itself, all of the bots command categories can be found in here, and they are located in the same way they are categorized under ~help.

#### Misc:

* Misc has all the different files that the bot needs to pull from, such as the avatar (which gets automatically uploaded to the Discord Developers Portal the first time the code is run), the rainbow bar emojis (which get automatically uploaded to a server Miza is in if it cannot find the emojis already), the code necessary for converting org files, computing math equations, finding time zones and etc. You can change the bots avatar and emojis if you want to; *but if you want the code to use them the same way, the filename must be kept the same.*


<a id="Support"></a>
## Support!

With that concludes the basic introduction of hosting Miza. The code is commented and explaining where everything is, so feel free to explore further to see what you can change, and if you have any questions, [Thomas Xin](https://github.com/thomas-xin) is your guy to ask!

[Read our Wiki!](https://github.com/thomas-xin/Miza/wiki) • [Join our Discord Support Server!](https://discord.gg/cbKQKAr) • [Check out our Website!](http://mizabot.xyz)

*The domain redirects to a webserver which includes: a command tester within the comforts of your browser, a free file host, and more!*


<a id="API"></a>
## API

Miza has a public API that has now been moved to [RapidAPI](https://rapidapi.com/thomas-xin/api/miza). Currently not all endpoints and possible features in the API are accessible from there, but it will be updated over time.


<a id="Credits"></a>
## Credits

Thanks to all the [contributers](https://github.com/thomas-xin/Miza/graphs/contributors), for helping Miza grow!

*Writing this README is [smudgedpasta](https://github.com/smudgedpasta), Miza's secondary bot owner! :3*

<br>

<p align="center">
Please support the development of Miza here if you enjoy her services, or would like access to her premium features!<br>
https://ko-fi.com/mizabot<br>
Miza has been free to use for 3 years now since the start of her development, but is quickly becoming more expensive to sustain. Any donations are greatly appreciated, and 100% will go towards supporting Miza's future!
</p>
