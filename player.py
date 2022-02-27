import discord, sys
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

    print("Playing", name.capitalize())

    #hakkab mängima
    async with ctx.typing():
        ctx.voice_client.play(discord.FFmpegPCMAudio(url), after=lambda e: print('Player error: %s' % e) if e else None)

    #tagasiside kasutajale
    await ctx.send(":musical_note: Mängin **" + name.capitalize() + "**")
    
if __name__ == '__main__':
    print("Käivita main.py fail")
    sys.exit()
