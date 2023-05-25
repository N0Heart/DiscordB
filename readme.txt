----------------READ ME------------------

REQUIRED LIBRARIES:

- Discord (contains basic discord development commands)
- Discord.ext (contains the libraries needed to create user commands for the bot to read)
- Requests (pulls API url from online)
- asyncio (foundation)
- yt_dlp (downloads the input youtube file)
- os (imports token file containing YOUR imported discord bot token / instructions below)
- dotenv (loads the environment file needed for os to import the bot token)
- PyNaCl (foundation)
- FFmpeg (converts downloaded youtube videos into audio mpeg files for the bot to play // Please see instructions below for FFMPEG installation as it can be tricky)

INSTALLATION/USE:


SETUP:

1) Create a .env file inside pythonProject2/venv and copy and paste the following:

DISCORD_TOKEN=

2) Copy your unique Discord bot token and paste it after the "=" with no spaces and no quotes

3) Make sure that you do not share this .env file with anyone unless they you want them to be able to manipulate the bot's actions as well. 
	Note: if you post this file or the token anywhere online, Discord will automatically and immediately change your token and you will have to repeat step 2.

4) On like 75 change "channel = bot.get_channel(xxxxxxxxxxxxxxxxxxxx)" to the channel ID of the chat server that you want the bot to alert when it comes online. You can find this by going into settings --> advanced --> Developer Mode = On. Then finding the channel you want it to go to, right click on it and then click on "copy channel ID". 


FFMPEG GUIDE:

FFMPEG requires you to have BOTH the library package installed and imported AND the ffmpeg.exe files (found here: https://www.gyan.dev/ffmpeg/builds/ ****get the full)
installed to the libary. I had to install all three .exe files to pythonProject2/venv/Scripts. Make sure you complete this step properly or you will not be able to use the music bot. Please note that you could be held liable for misuse of copyright protected audio. 


GENERAL USE:

- You can manipulate/change/remove/add to my template tuples as needed. These are words the bot will look for in other user's messages and will respond accordingly.
	For example: change the "banned" words to actual swear words/ words you don't want being said. 
- To add more words, just add a comma after the last word's apostrophe and type the new word in quotes.

- You can change what the bot's response to words in these lists are by changing the text strings that follow "if any(word in message.content.lower() for word in #list):
        await message.channel.send(" 

- The bot can generate a random insult from online that can be inserted into responses using the get_insult function. Type $insult to have to send one into the text channel.

- To play music:
	- make sure you are in a discord audio channel and that the bot is not already playing music in your channel.
	- type !play followed by a link to a YouTube song

- To pause music:
	- type !pause

- To select a new song:
	- type !stop
	- repeat step 1

- Type "!info" to get information about the server and channel you are in.

- Type "!music" to get instructions on how to use the music player.

- Type "!wave" followed by the @ of the user you would like to wave at.




