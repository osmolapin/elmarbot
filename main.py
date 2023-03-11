import discord, player, check, video_url
from discord.ext import commands
from random import randint

SKYPLUS_URL = "https://skymedia-live.bitflip.ee/SKYPLUS"
ELMAR_URL = "https://router.euddn.net/8103046e16b71d15d692b57c187875c7/elmar.mp3"
RINGFM_URL = "https://sc2.treraadio.ee/ringfm"
ROCKFM_URL = "https://skymedia-live.bitflip.ee/rck"
VOMBAFM_URL = "http://c4.radioboss.fm:8123/live"


TOKEN = check.isFile()

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    activity = discord.Game(name="Raadio Elmar", type=2)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot online")

@client.event
async def on_message(msg):
    ctx = await client.get_context(msg)

    if ".mangi" in msg.content:
        title, url = video_url.get(msg.content)
        await player.play(ctx, url, await check.inVoice(ctx, client), await check.isPlaying(ctx), title)
    
    await client.process_commands(msg)

@client.command()
async def abi(ctx):
    embed=discord.Embed(title="Käsud", color=discord.Color.gold())
    embed.add_field(name=".laula", value="- Laulab parimat raadiot maailmas.", inline=False) 
    embed.add_field(name=".skyplus", value="- Laulab mitte nii head raadiot kui Raadio Elmar.", inline=False) 
    embed.add_field(name=".ringfm", value="- Laulab kõige lambisemat raadiot.", inline=False) 
    embed.add_field(name=".rockfm", value="- Laulab rock efem.", inline=False) 
    embed.add_field(name=".vombafm", value="- Laulab võmbast.", inline=False)
    embed.add_field(name=".mangi", value="- Mängib youtube lingi järgi või otsib video ja mängib seda.", inline=False) 
    embed.add_field(name=".lahku", value="- Lahkub kõnest.", inline=False) 
    await ctx.send(embed=embed)
  
@client.command()
async def lahku(ctx):
    if not await check.inVoice(ctx, client):
        await ctx.send("Ma olen juba lahkunud tola!")
    else:
        print("Leaving voice channel")
        await ctx.send("Tsauki!")
        await ctx.voice_client.disconnect()

@client.command()
async def laula(ctx):
    await player.play(ctx, ELMAR_URL, await check.inVoice(ctx, client), await check.isPlaying(ctx), "Elmar")

@client.command()
async def skyplus(ctx):
    await player.play(ctx, SKYPLUS_URL, await check.inVoice(ctx, client), await check.isPlaying(ctx), "Skyplus")

@client.command()
async def ringfm(ctx):
    await player.play(ctx, RINGFM_URL, await check.inVoice(ctx, client), await check.isPlaying(ctx), "Ring Fm")

@client.command()
async def rockfm(ctx):
    await player.play(ctx, ROCKFM_URL, await check.inVoice(ctx, client), await check.isPlaying(ctx), "Rock Fm")

@client.command()
async def vombafm(ctx):
    await player.play(ctx, VOMBAFM_URL, await check.inVoice(ctx, client), await check.isPlaying(ctx), "Võmba Fm")

@client.command()
async def mangi(ctx):
    pass

client.run(TOKEN)
