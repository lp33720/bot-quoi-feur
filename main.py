import json
from concurrent.futures import process
from pathlib import Path
import discord

##############

# PATH = Path("/home/aurnytoraink/Bot/Coiffeur")
from discord.ext import commands
from discord.ext.commands import bot

PATH = Path("E:\Dev\Bot_QuoiFeur")
# Insérer l'adresse où se situe votre dossier

TOKEN = json.loads(open(PATH / "config.json", 'rb').read())["token"]

#############
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # Setting `Playing ` status
    bot.change_presence(activity=discord.Game(name="Manger Drakior"))


@client.event
async def on_message(message):
    # Évite que le bot intercepte ces propres messages
    if message.author == client.user:
        return

    # Prise en charge des majuscules et mininuscules
    # + les textes déformés comme "qUoiiiiiiiiiiiiiiiii ?"
    if message.content.lower().endswith('quoi'):
        await message.channel.send("Feur")
    if message.content.lower().endswith('quoi ?'):
        await message.channel.send("Feur")
    if message.content.lower().endswith('quoi?'):
        await message.channel.send("Feur")


client.run(TOKEN)
