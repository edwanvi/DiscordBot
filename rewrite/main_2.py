"""
Rewrite of magi-bot to use the command extension.
"""
print("Importing discord")
import discord
from discord.ext import commands
print("Importing asyncio")
import asyncio

# create bot
bot = commands.Bot(command_prefix='[] ', description="One hell of a dank meme.")

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------------")

@bot.command(description='Check for responsiveness.')
async def robot():
    """Pings the robot."""
    await bot.say("BLEEP BLOOP")

@bot.command(description="Echoes a message. No recursing!")
async def echo(*, message: str):
    if not (message.startswith(bot.command_prefix)):
        await bot.say(message)

bot.load_extension("memeage")
bot.load_extension("control")
bot.run('token')
