----------------READ ME------------------

REQUIRED LIBRARIES:

- Discord.py (contains basic discord development commands)
	"pip install discord.py"
- Discord.ext (contains the libraries needed to create user commands for the bot to read)
- Requests (pulls API url from online)
- asyncio (foundation)
- yt_dlp (downloads the input youtube file)
	"pip install yt-dlp
- yt_dlp_progress (tracks player's spot in the file)
	"pip install yt-dlp-progress"
- PyNaCl (foundation)
	"pip install PyNaCl"
- FFmpeg (converts downloaded youtube videos into audio mpeg files for the bot to play // Please see instructions below for FFMPEG installation as it can be tricky)
	"pip install ffmpeg"

INSTALLATION/USE:


SETUP:

1) You must set up your own bot on the Discord developer portal site. This will genereate you a token in which the bot uses to gain access to the servers that you want it to gain access to. You can follow 
the first ~4.5 minutes of this video:
https://www.youtube.com/watch?v=hoDLj0IzZMU&ab_channel=Indently to see how your bot should be set up. Once you have your token pasted, be sure to copy it into a local text file somehwere becuase it will only be displayed on the developer portal once. If you have completed step one correctly, your bot should be displayed as a member of your server, but offline. 
Note: if you post the token anywhere online, Discord will automatically and immediately change your token and you will have to repeat step 1.
2) On the very last line of the program, replace the "xxx" with your discord token surrounded by "quotes".
	example: bot.run("YOUR-DISCORD-TOKEN-HERE")
3) On line 75 change "channel = bot.get_channel(xxxxxxxxxxxxxxxxxxxx)" to the channel ID of the chat server that you want the bot to alert when it comes online. You can find this by going into settings --> advanced --> Developer Mode = On. Then finding the channel you want it to go to, right click on it and then click on "copy channel ID". 
4) Follow the steps mentioned below about setting up FFMPEG in order to get the music player working. The bot will work regardless of whether or not the music player is set up.
5) You can now test that the bot was set up correctly by running the program. If all goes well, you should get the welcome/greeting message printed in your console as well as in the Discord text channel you copied the ID
to in step 3. The bot will then come online in your discord server. 
6x) It is strongly reccomended that you change the values of my "lists" (tuples) in lines 30 through 38 as these are the words that the bot will be "looking" for in the text channels. You will also want to change the 
responses that the bot gives by looking for the matching function under the "async def on_message" class and changing the text that is in quotes.


FFMPEG GUIDE:

FFMPEG requires you to have BOTH the library package installed and imported as well as the ffmpeg.exe files (found here: https://www.gyan.dev/ffmpeg/builds/ ****get the full) Note* You will need 7zip to open the files.
LINK: https://www.7-zip.org/download.html 
in the folder of the libary. Inside of the "Bin" folder that you just downloaded you should find three .exe files. This is all we need. Drag all three .exe files to 
DiscordB(this name could be different)/venv/Scripts. Make sure you complete this step properly or you will not be able to use the music bot. Please note that you could be held liable for misuse of copyright protected audio.  


GENERAL USE:

- You can manipulate/change/remove/add to my template tuples as needed. These are words the bot will look for in other user's messages and will respond accordingly.
	For example: change the "banned" words to actual swear words/ words you don't want being said. 
- To add more words, just add a comma after the last word's apostrophe and type the new word in quotes.

- You can change what the bot's response to words in these lists are by changing the text strings that follow "if any(word in message.content.lower() for word in #list):
        await message.channel.send(" 

- The bot can generate a random insult from online that can be inserted into responses using the get_insult function. Type $insult to have to send one into the text channel.

- To play music:
	- make sure you are in a discord audio channel and that the bot is not already playing music in your channel.
	- type !play followed by a link to a YouTube song. (I have found that other sites such as soundcloud will work as well. Feel free to experiment with other websites. Just use a link that goes directly
	to the song.

- To pause music:
	- type !pause

- To select a new song:
	- type !stop
	- repeat step 1
Note: Sometimes the bot will return an error in the text channel but it should still join the voice channel and play the audio.\

Basic Commands:

- Type "!info" to get information about the server and channel you are in.

- Type "!music" to get instructions on how to use the music player.

- Type "!wave" followed by the @ of the user you would like to wave at.

- Type "!ban" to get a list of words that are not allowed in the server. 



