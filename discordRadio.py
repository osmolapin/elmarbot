import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

#ctx - bot, url - raadio url (string) , in_voice - kas on kõnes(boolean) , is_playing - kas mängib(boolean) , name - raadio nimi(boolean)
async def play(ctx, url, in_voice, is_playing, name):

    #joinib voice kanalisse
    if not in_voice:
        channel = ctx.author.voice.channel
        print("Joining a voice channel")
        await channel.connect()

    #kui mängib paneb eelmise raadio kinni
    if is_playing:
        ctx.voice_client.stop()

    #konsooli input
    if name.lower() == "elmar":
        print("Playing Elmar")
    elif name.lower() == "skyplus":
        print("Playing Skyplus")

    #hakkab mängima
    async with ctx.typing():
        ctx.voice_client.play(discord.FFmpegPCMAudio(url), after=lambda e: print('Player error: %s' % e) if e else None)

    #tagasiside kasutajale
    if name.lower() == "elmar":
        await ctx.send("Davai!")
    elif name.lower() == "skyplus":
        await ctx.send('Elmar on parem!')