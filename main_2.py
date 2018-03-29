"""
Rewrite of magi-bot to use the command extension.
"""
print("Importing discord")
import discord
from discord.ext import commands
print("Importing asyncio")
import asyncio
import extrautils

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
    if not (message.startswith(bot.command_prefix)) and not message.lower().startswith("the human mind loves repetition"):
        await bot.say(message)
    else:
        pass

@bot.command(description="For 3494 members only", pass_context=True)
async def competition(ctx, member: discord.Member = None):
    if (member is None and ctx.message.server.id == "286174293006745601"):
        member = ctx.message.author
    await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name="Competition"))
    await bot.say("Gave {} the competition role".format(member.mention))

extensions = ["memeage", "control", "chattery", "dungeons"]
for name in extensions:
    print("Loading " + name)
    bot.load_extension(name)

print("Running bot...")
token = extrautils.getCreds('creds.txt', 'token')
bot.run(token)
