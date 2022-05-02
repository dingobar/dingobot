# bot.py
import os

import discord
from discord.message import Message

import eurovision

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")
    print("HI")


@client.event
async def on_message(message: Message) -> None:
    if message.author.bot:
        return
    general = client.get_channel(853711410931302404)
    if eurovision.message_is_about_eurovision(message.content):
        reply = f"Eurovision starter om {eurovision.time_until_eurovision()}"
        await general.send(reply)


client.run(TOKEN)
