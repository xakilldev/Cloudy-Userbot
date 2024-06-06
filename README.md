<p align="center">

    </a>

    <br>

    <b>Cloudy-Userbot</b>

    <br>

    <b>Telegram userbot with the easiest installation</b>

    <br>

    <a href='https://github.com/Cloudy-Userbot/Cloudy-Userbot#installation'>

        Installation

    </a>

    <br>

</p>









<h1>About</h1>

<p>Cloudy-Userbot is a Telegram userbot



<h1>Installation</h1>

<h2>lavHost</h2>



<a href="https://t.me/lavhostbot?start=RHJhZ29u"><img src="https://f.lavhost.ml/images/install_to_lavhost.png"></a>





<h2>Linux, Termux (use <a href='https://f-droid.org/en/packages/com.termux/'>f-droid</a> version) and Windows [only wsl]</h2>



<pre><code>apt-get upgrade -y && apt-get update && apt install git && git clone https://github.com/Cloudy-Userbot/Cloudy-Userbot.git && cd Cloudy-Userbot/ && bash install.sh

</code></pre>



<h2>macOS [<a href='https://brew.sh'>brew</a>]</h2>

<pre><code>brew install git && git clone https://github.com/Cloudy-Userbot/Cloudy-Userbot.git && cd Cloudy-Userbot && brew install python@3.8 && pip3 install --upgrade pip && pip3 install wheel && brew install ffmpeg && pip3 install -r requirements.txt && pip3 install -U 'pytgcalls[pyrogram]' && echo Enter your db_url: && read uservar && python3 install.py $uservar

</code></pre>



<p>Next enter mongo_db_url (<a href='https://telegra.ph/How-to-get-Mongodb-URL-and-login-in-telegram-08-01'>How to get Mongodb_URL and login in telegram</a>)</p>



<pre><code>.help</code> (in telegram chat)</pre>



Subsequent launch:



<pre><code>cd Cloudy-Userbot/</code></pre>



<pre><code>python3 main.py</code></pre>





<h1>Custom modules</h1>





<p>To add your module to the bot, create a pull request in the <a href='https://github.com/Cloudy-Userbot/custom_modules/'>custom_modules</a> repository</p>



```python3

from pyrogram import Client, filters

from pyrogram.types import Message



from utils.misc import modules_help, prefix





# if your module has packages from PyPi



# from utils.scripts import import_library

# example_1 = import_library("example_1")

# example_2 = import_library("example_2")



# import_library() will automatically install required library

# if it isn't installed





@Client.on_message(filters.command("example_edit", prefix) & filters.me)

async def example_edit(client: Client, message: Message):

    await message.edit("<code>This is an example module</code>")





@Client.on_message(filters.command("example_send", prefix) & filters.me)

async def example_send(client: Client, message: Message):

    await client.send_message(message.chat.id, "<b>This is an example module</b>")





# This adds instructions for your module

modules_help["example"] = {

    "example_send": "example send",

    "example_edit": "example edit",

}



# modules_help["example"] = { "example_send [text]": "example send" }

#                  |            |              |        |

#                  |            |              |        └─ command description

#           module_name         command_name   └─ optional command arguments

#        (only snake_case)   (only snake_case too)

```



</nav>
