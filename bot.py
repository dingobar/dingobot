# bot.py
import os

import discord
from discord.ext import commands
from discord.message import Message
from discord_slash import SlashCommand, SlashContext

import eurovision

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="/", intents=intents)
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    print("HI")


@bot.event
async def on_message(message: Message) -> None:
    if message.author.bot:
        return
    general = bot.get_channel(853711410931302404)
    if eurovision.message_is_about_eurovision(message.content):
        reply = f"Eurovision starter om {eurovision.time_until_eurovision()}"
        await general.send(reply)


@slash.slash(name="test")
async def test_command(context: SlashContext):
    await context.send("Hello!")


bot.run(TOKEN)
