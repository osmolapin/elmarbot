import discord, player, sys
from discord.ext import commands

def isFile():
    try:
        file = open("TOKEN.txt", "r")
        return file.read()
    except:
        print("Puudub fail nimega 'TOKEN.txt'\n Luuakse fail\n Sisestage sinna Boti token.")
        file = open("TOKEN.txt", "w")
        file.write("Kustutada kõik ära ja kopeerida token 1. reale")
        file.close()
        sys.exit()

async def isPlaying(ctx):
    try:
        if ctx.voice_client.is_playing():
            return True
    except:
        return False

async def inVoice(ctx, client):
    if ctx.guild.voice_client in client.voice_clients:
        return True
    else:
        return False

if __name__ == '__main__':
    print("Käivita main.py fail")
    sys.exit()
