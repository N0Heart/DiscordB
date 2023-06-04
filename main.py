# Imported Libraries #
import discord
import requests
import yt_dlp as youtube_dl
import asyncio
from discord.ext import commands

# Reassignment Keys #

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Blank Client Dictionary #
voice_clients = {}

# Music Options #
yt_dl_opts = {'format': 'bestaudio/best', 'noplaylist': 'False'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': '-vn'}


# Functions #
# Gets random insult from evilinsult api #
def get_ins():
    response = requests.get("https://evilinsult.com/generate_insult.php?")
    quote = response.text
    return quote


def get_comp():
    response = requests.get("https://complimentr.com/api")
    data = response.json()
    compliment = data["compliment"]
    capitalize = compliment.capitalize()
    return capitalize + "."


typing = ["fast", "speed", "typing", 'keyboard', "switches", "quick", "type"]

banned = ["frig", "shiz", "sad", "fudge", "gun", "nerd", "geek"]

Max = ["max", "weird", "bird", "freak", "mux", "straus", "sam", "frodo"]

greetings = ["Hi", "hi", "hello", "sup", "whats good", "whats up", "wya"]

doug = ["doug", "thomas", "tommy", "tom", "doog"]

commands = ["!ban - lists banned words", "!comp - generates a random compliment", "!info - lists current server info",
            "!music - music player instructions", "!wave - wave at a user"]


# Client Events #
@bot.command()
async def ban(ctx):
    await ctx.send(f"Banned words are: {', '.join(banned)}")


@bot.command()
async def comp(ctx):
    quote = get_comp()
    await ctx.send(quote)
    

@bot.command()
async def comp(ctx):
    quote = get_ins()
    await ctx.send(quote)


@bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)


@bot.command()
async def music(ctx):
    await ctx.send(
        f"{ctx.author.mention} You can play music by typing !play followed by a link to a YouTube song you want to "
        f"hear.\nYou can pause by typing !pause.\nYou can play a new song by typing !stop and then repeating the "
        f"first step.")


@bot.command()
async def wave(ctx, arg):
    await ctx.send(f" extends a friendly and robotic wave at {arg} on behalf of {ctx.author.mention}.")


@bot.event
async def on_ready():
    print("Holy smokes I'm logged in to Discord as {0.user}! Get ready for extreme moderation.".format(bot))
    channel = bot.get_channel(1102412567659425835)
    await channel.send(
        "Holy smokes I'm logged in to Discord as {0.user}! Get ready for extreme moderation.".format(bot))


@bot.event
async def on_message(message):
    # Shortening Directories #
    user = message.author
    # Checks that the message wasn't sent by the bot #
    if message.author == bot.user:
        return

    # If a user mentions the bot #
    if bot.user.mentioned_in(message):
        await message.channel.send(
            f"Hello {user.mention}! How are you doing today? Want me to play some music? Just type $play followed by a "
            "space and a YouTube link to the media you want to hear!")

    # If a user talks about Thomas #
    if any(word in message.content.lower() for word in doug):
        await message.channel.send(
            "Thomas is working towards becoming the most powerful programmer in the history of the nation. At the "
            "rate he is going, I suspect he will find a way to convert himself into a half-human half-AI cyborg, "
            "and it's all thanks to the folks that work for the course that taught him how to do it.")

    # Creates a random insult #
    if message.content.lower().startswith("!insult"):
        quote = get_ins()
        await message.channel.send(quote)
    # Banned word action #
    if any(word in message.content.lower() for word in banned):
        get_ins()
        s = get_comp()
        await message.channel.send(
            f"{user.mention} {s} It is so important that you understand that this kind of language is absolutely NOT "
            f"allowed in my discord server. Try that again and you will be permanently removed.")

    # Brags about Thomas' typing speed #
    if any(word in message.content.lower() for word in typing):
        await message.channel.send(
            f"{user.mention} Have you seen how fast Thomas can type on his Keychron Q5 though? Check this out:"
            f"https://data.typeracer.com/misc/badge?user=slylar45")

    # Talks about max #
    if any(word in message.content.lower() for word in Max):
        await message.channel.send(
            "Max Straus, otherwise known as the only man able to outrun himself, was last seen in this server over "
            "two months ago on a cold, March evening. We do not know when he is expected to return, "
            "but our anxiousness towards it is overwhelming.")

    # Responds to greetings #
    if any(word in message.content.lower() for word in greetings):
        await message.channel.send(
            "Hello {user.mention]! How are you doing today? Want me to play some music? Just type !play followed by a "
            "space and a YouTube link to the media you want to hear!")

    # Music Player #
    if message.content.lower().startswith("!play"):

        try:
            voice_client = await message.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except:
            await message.channel.send("There could be an error playing the file. Give me a second...")

        try:
            url = message.content.split()[1]

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

            voice_clients[message.guild.id].play(player)
        except Exception as err:
            await message.channel.send(f"{err}.")

    if message.content.lower().startswith("!pause"):
        try:
            voice_clients[message.guild.id].pause()
        except Exception as err:
            print(err)

    # This resumes the current song playing if it's been paused #
    if message.content.lower().startswith("!resume"):
        try:
            voice_clients[message.guild.id].resume()
        except Exception as err:
            print(err)

    # This stops the current playing song #
    if message.content.lower().startswith("!stop"):
        try:
            voice_clients[message.guild.id].stop()
            await voice_clients[message.guild.id].disconnect()
        except Exception as err:
            print(err)
    await bot.process_commands(message)


# Client Key - DO NOT TOUCH OR EDIT BELOW THIS LINE - #
bot.run("xxx")
