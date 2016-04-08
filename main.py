import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!robot'):
        await client.send_message(message.channel, 'BLEEP BLOOP')
    elif message.content == '!cease':
        await client.send_message(message.channel, 'Authenticating...')
        author = message.author
        authorname = author.name
        if authorname == 'magi093':
            await client.send_message(message.channel, 'Ceasing.')
            await client.logout()
        else:
            await client.send_message(message.channel, "Sorry, you don't have the ability to do that.")

client.run('tkdberger@gmail.com', 'full_leobitz')
