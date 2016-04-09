import discord
import asyncio
import extrautils
import commands

# create a new Client for the bot to run on.
client = discord.Client()
# Open the file that contains the username and password for the account.
username = extrautils.getCreds('creds.txt', 'username')
password = extrautils.getCreds('creds.txt', 'password')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)


@client.event
async def on_message(message):
    if message.content.startswith('?test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages, '.format(counter) + message.author.name)

    elif message.content.startswith('?sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('?robot'):
        await client.send_message(message.channel, 'BLEEP BLOOP')

    elif message.content.startswith('?bug'):
        await client.send_message(message.channel, "It's not a bug, it's a feature.")

    elif message.content == '?cease':
        await client.send_message(message.channel, 'Authenticating...')
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
        if echoverify == '?echo ' or echoverify == '?echo':
            return
        else:
            await client.send_message(message.channel, echo)

    # run commands from commands.py
    elif message.content.startswith("?help"):
        await commands.send_help(client, message)
    elif message.content.startswith("?heythere"):
        await commands.hey_buddy(client, message)
    elif message.content.startswith("?github"):
        github_name = message.content[8:]
        await commands.github(client, message, github_name)

client.run(username, password)