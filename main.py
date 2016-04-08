import discord
import asyncio

# create a new Client for the bot to run on.
client = discord.Client()
# Open the file that contains the username and password for the account.
datafile = open('creds.txt')
for line in datafile:
    if line.startswith('u:'):
        username = line[2:]
    elif line.startswith('p:'):
        password = line[2:]
    else:
        print("Input file not valid. Terminating.")
        exit()

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
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

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
        authorname = author.name
        if authorname == 'magi093':
            await client.send_message(message.channel, 'Ceasing.')
            await client.logout()
        else:
            await client.send_message(message.channel, "Sorry, you don't have the ability to do that.")

    elif message.content.startswith('?echo'):
        echo = message.content[6:]
        await client.send_message(message.channel, echo)

client.run(username, password)
