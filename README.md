# Discord Bot Instructions

![dashgiffy](https://github.com/N0Heart/DiscordB/blob/main/videoDemo.gif)

## REQUIRED LIBRARIES/Tools:

- Discord.py (contains basic discord development commands) // v2.2.3
- terminal use: "pip install discord.py"
- Discord.ext (comes with Discord.py/contains the libraries needed to create user commands for the bot to read)
- Requests (pulls API url from online) // v2.30
 - terminal use: "pip install requests"
- asyncio (used for music player) // v3.4.3
 - terminal use:	"pip install asyncio"
- yt_dlp (downloads the input youtube file) // v2023.3.4
 - terminal use:	"pip install yt-dlp"
- yt_dlp_progress (tracks player's spot in the file) // v0.0.2
 - terminal use:	"pip install yt-dlp-progress"
- PyNaCl (foundation) // v1.5
 - terminal use:	"pip install PyNaCl"
- FFmpeg (converts downloaded youtube videos into audio mpeg files for the bot to play // Please see instructions below for FFMPEG installation as it can be tricky) // v1.4
 - terminal use:	"pip install ffmpeg"
### Non-Library Tools:
- 7zip : https://www.7-zip.org/download.html 
- FFMPEG .exe files : https://www.gyan.dev/ffmpeg/builds/ (get the "Full" version)
- A Discord account : https://support.discord.com/hc/en-us/articles/360033931551-Getting-Started
- A Discord server that you own and manage : https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server-
- Running on Windows 10, should work with Mac OS, untested on linux.
- Running Python 3.10


## SETUP:

1) You must set up your own bot on the Discord developer portal site. This will genereate you a token in which the bot uses to gain access to the servers that you want it to gain access to. 
 	- You can follow the first ~4.5 minutes of this video: https://www.youtube.com/watch?v=hoDLj0IzZMU&ab_channel=Indently to see how your bot should be set up. 
 	- For general purposes, you want your bot to have admin priveleges under the Oath2 tab. 
	- Once you have your token copied, be sure to paste it into a local text file somehwere becuase it will only be displayed on the developer portal once. 
	- If you followed the video, you should use the invite link that you generated in the Dev portal to invite the bot to your server.
	- After inviting, your bot should be displayed as a member of your server, but offline. 
	- Note: if you post the token anywhere online, Discord will automatically and immediately change your token and you will have to repeat step 1.
2) On the very last line of the program, replace the "xxx" with your discord token surrounded by "quotes".
	- example: bot.run("YOUR-DISCORD-TOKEN-HERE")
3) On line 75 change "channel = bot.get_channel(xxxxxxxxxxxxxxxxxxxx)" to the channel ID of the chat server that you want the bot to alert when it comes online. 
 	- You can find this by going into settings --> advanced --> Developer Mode = On. Then finding the channel you want it to go to, right click on it and then click on "copy channel ID". 
5) Follow the steps mentioned below about setting up FFMPEG in order to get the music player working. The bot will work regardless of whether or not the music player is set up.
6) You can now test that the bot was set up correctly by running the program. If all goes well, you should get the welcome/greeting message printed in your console as well as in the Discord text channel you copied the ID
to in step 3. The bot will then come online in your discord server. 
6x) It is strongly reccomended that you change the values of my lists in lines 30 through 38 as these are the words that the bot will be "looking" for in the text channels. You will also want to change the 
responses that the bot gives by looking for the matching function under the "async def on_message" class and changing the text that is in quotes.
	- For example:
		On lines 123 and 124, change the text within the quotes to be what you want your bot to tell users when they use a word in the "banned" list. You can add or remove as many of these functions as you want, so long as they have a list of words at the top to refer to.
7x) There are two preset functions called get_ins and get_comp that will generate a random insult or compliment from online that the bot can then inject into its messages. Feel free to add/remove/change these to pull any other type of information from a third party API. Be sure to follow the documentation that is providided on their website in order to get the text to display properly.

## FFMPEG GUIDE:

FFMPEG requires you to have BOTH the library package installed and imported as well as the ffmpeg.exe files (found here: https://www.gyan.dev/ffmpeg/builds/ ****get the full) Note* You will need 7zip to open the files.
LINK: https://www.7-zip.org/download.html 
installed in the venv folder of the project. 
Inside of the "Bin" folder that you just downloaded you should find three .exe files. This is all you need. Drag all three .exe files to 
DiscordB(this name could be different if you change the project name)/venv/Scripts. Make sure you complete this step properly or you will not be able to use the music bot. Please note that you could be held liable for misuse of copyright protected audio.  


## GENERAL USE:

- You can manipulate/change/remove/add to my template lists as needed. These are words the bot will look for in other user's messages and will respond accordingly.
	
	For example: change the "banned" words to actual swear words/ words you don't want being said. 

- To add more words, just add a comma after the last word's apostrophe and type the new word in quotes.

- You can change what the bot's response to words in these lists are by changing the text strings that follow "if any(word in message.content.lower() for word in #list):
        await message.channel.send(" 

- The bot can generate a random insult from online that can be inserted into responses using the get_insult function. Type !ins to have to send one into the text channel.

- To play music:
	- make sure you are in a discord audio channel and that the bot is not already playing music in your channel.
	- type !play followed by a link to a YouTube song. (I have found that other sites such as soundcloud will work as well. Feel free to experiment with other websites. Just use a link that goes directly
	to the song.

- To pause music:
	- type !pause

- To select a new song:
	- type !stop
	- repeat step 1

Note: Sometimes the bot will return an error in the text channel but it should still join the voice channel and play the audio.

## Basic Commands:

- Type "!server" to get information about the server and channel you are in.

- Type "!music" to get instructions on how to use the music player.

- Type "!wave" followed by the @ of the user you would like to wave at.

- Type "!ban" to get a list of words that are not allowed in the server.

- Type "!ins" to make the bot generate a random insult. (Be warned, some of these can get pretty offensive)

- Type "!comp" to make the bot generate a random compliment.

## Works Cited:
- How I began learning to set up basic bots: https://www.youtube.com/watch?v=fU-kWx-OYvE&ab_channel=Indently
- How I learned to actually use the Discord API myself. Almost all of your questions can be answered with the official documentation: https://discordpy.readthedocs.io/en/stable/api.html#message

