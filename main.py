import discord
import asyncio
import extrautils
import commands

# create a new Client for the bot to run on.
print("magi-bot v. 1.0 starting up")
client = discord.Client()
# Open the file that contains the username and password for the account.
username = extrautils.getCreds('creds.txt', 'username')
password = extrautils.getCreds('creds.txt', 'password')
token = extrautils.getCreds('creds.txt', 'token')
with open("magi093.png", 'rb') as f:
    profile = f.read()

@client.event
async def on_ready():
    print('Logged in as ' + client.user.name)
    print('Id: ' + client.user.id)
    await client.edit_profile(avatar=profile)

@client.event
async def on_message(message):
    if message.content.startswith('?test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages, @'.format(counter) + message.author.name)

    elif message.content.startswith('?sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('?robot'):
        await client.send_message(message.channel, 'BLEEP BLOOP')

    elif message.content.startswith('?bug'):
        await client.send_message(message.channel, "It's not a bug, it's a feature.")

    elif message.content == '?cease':
        author = message.author
        authorname = author.id
        if authorname == '164342765394591744':
            await client.send_message(message.channel, 'Ceasing.')
            await client.logout()
        else:
            await client.send_message(message.channel, "Sorry, you don't have the ability to do that.")

    elif message.content.startswith('?echo'):
        echo = message.content[6:]
        echoverify = message.content[6:12]
        if echoverify == '?echo ' or echoverify == '?echo' or echo == '':
            return
        else:
            await client.send_message(message.channel, echo)
    elif message.content.startswith('?w'):
        await client.send_message(message.channel, "wwwwwwwwwwwwwww", tts=True)

    # run commands from commands.py
    elif message.content == "?help":
        await commands.send_help(client, message)
    elif message.content.startswith("?heythere"):
        await commands.hey_buddy(client, message)
    elif message.content.startswith("?github"):
        github_name = message.content[8:]
        await commands.github(client, message, github_name)
    elif message.content.startswith("?source"):
        await commands.source(client, message)
    elif message.content.startswith("?info"):
        await commands.getUserInfo(client, message)
    # IDEA: Shorten this somehow. maybe a function that returns true if all this
    elif message.content.startswith("++voice") or message.content.startswith("++request"):
        if message.channel.id == "225619147046780930":
            print(message.author.name + " tried to call ++voice or ++request in #general.")
            warnmsg = await client.send_message(message.channel, "Please do not [ACTION:POST] [ABSTRACT:THEMES] [LOCATION:HERE]. [ENTITY:HITLERMOD] does not [ACTION:LIKE] that.")
            try:
                await client.delete_message(message)
            except discord.Forbidden:
                await client.send_message(message.channel, "Please give the bot the permission to delete messages to use this command.")
            await asyncio.sleep(5)
            client.delete_message(warnmsg)

# client.run(username, password)
# Trying the Oauth2 game.
client.run(token)
