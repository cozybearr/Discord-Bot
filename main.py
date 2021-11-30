from ytvids import mp3_download
from MusicBase import *
from apikeys import *
import discord
import asyncio
import os
import requests
import json
from discord.ext import commands
from discord import FFmpegPCMAudio

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='v/', intents=intents)


# Embed pages
page1 = discord.Embed(
    title="Finneas",
    description='\n'.join(Finneas),
    colour=0x34ebe1)
page2 = discord.Embed(title="Ed Sheeran",
                      description='\n'.join(Edsheeran),
                      colour=0x34ebe1)
page3 = discord.Embed(title="Charlie Puth",
                      description="Page 3",
                      colour=0x34ebe1)


client.help_pages = [page1, page2, page3]


queues = {}


def check_queue(ctx, id):
    if queues[id] != []:
        voice = ctx.guild.voice_client
        src = queues[id].pop(0)
        voice.play(src)


async def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q']
    author = json_data[0]['a']
    return(quote, author)


async def _getCat():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    json_data = json.loads(response.text)
    url = json_data[0]['url']
    return url


# ===================================== MAIN EVENT =================================================


@client.event
async def on_ready():
    print("JUPYTER IS ON THE LINE!")
    print("=======================")


# ===================================== MAIN COMMANDS =================================================


@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am the draftbot")


@client.command()
async def inspire(ctx):
    quote, author = await(get_quote())

    embedded_q = discord.Embed(title="Inspiring quote", color=0x03FDFC,
                               description=f'"{quote}" \n-- {author}')

    image_url = await _getCat()

    embedded_q.set_image(url=image_url)

    await ctx.send(embed=embedded_q)


@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        await ctx.send("💫🌠Jupyter has joined")
        voice.play(discord.FFmpegPCMAudio(
            executable="C:/FFmpeg/ffmpeg.exe", source="Musics/finneas.mp3"))
    else:
        await ctx.send("🪄You are not in a voice channel, you must be in a voice channel to run this command!")


@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("💫🌠Jupyter has left!")
    else:
        await ctx.send("📢I am not in a voice channel!")


@client.command(pass_content=True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('No song is playing')


@client.command(pass_content=True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('No song is paused at the moment!')


@client.command(pass_content=True)
async def play(ctx, arg):
    voice = ctx.guild.voice_client
    song = 'Musics/' + arg + '.mp3'
    src = FFmpegPCMAudio(executable="C:/FFmpeg/ffmpeg.exe", source=song)
    voice.play(src, after=lambda x=None: check_queue(
        ctx, ctx.message.guild.id))
    await ctx.send('🎶Playing ' + str(arg) + ' 🎼🎧')


@client.command(pass_content=True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command(pass_content=True)
async def queue(ctx, arg):
    voice = ctx.guild.voice_client
    song = 'Musics/' + arg + '.mp3'
    src = FFmpegPCMAudio(executable="C:/FFmpeg/ffmpeg.exe", source=song)

    guild_id = ctx.message.guild.id

    if guild_id in queues:
        queues[guild_id].append(src)
    else:
        queues[guild_id] = [src]

    print(queues)
    await ctx.send("Added " + str(arg) + ' to queue')


# ========================================Embedding=================================================


# @client.command()
# async def embed(ctx):
#     embed = discord.Embed(title='Dog', url="https://google.com",
#                           description="This is me!", color=0x34ebe1)
#     embed.set_author(name=ctx.author.display_name, url='https://www.instagram.com/nauqh_21/',
#                      icon_url=ctx.author.avatar_url)
#     embed.set_thumbnail(
#         url="https://upload.wikimedia.org/wikipedia/commons/4/4d/Beautiful_landscape.JPG")
#     embed.add_field(name='Field 1', value='Pr0', inline=True)
#     embed.add_field(name='Field 2', value='Vjp', inline=True)
#     embed.set_footer(text='Thank you for reading')
#     await ctx.send(embed=embed)


@client.command()
async def album(ctx):
    # skip to start, left, right, skip to end
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"]
    current = 0
    msg = await ctx.send(embed=client.help_pages[current])

    for button in buttons:
        await msg.add_reaction(button)

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add",
                                                   check=lambda reaction,
                                                   user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

        except asyncio.TimeoutError:
            return print("test")

        else:
            previous_page = current
            if reaction.emoji == u"\u23EA":
                current = 0

            elif reaction.emoji == u"\u2B05":
                if current > 0:
                    current -= 1

            elif reaction.emoji == u"\u27A1":
                if current < len(client.help_pages)-1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = len(client.help_pages)-1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=client.help_pages[current])


# =================================================TEST=======================================
@client.command()
async def pages(ctx):
    contents = ["This is page 1!", "This is page 2!",
                "This is page 3!", "This is page 4!"]
    pages = 4
    cur_page = 1
    message = await ctx.send(f"Page {cur_page}/{pages}:{contents[cur_page-1]}")
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(content=f"Page {cur_page}/{pages}:n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(content=f"Page {cur_page}/{pages}:n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break
            # ending the loop if user doesn't react after x seconds

client.run(BOTTOKEN)
