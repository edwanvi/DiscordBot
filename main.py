print("Importing discord")
import discord
print("Importing asyncio")
import asyncio
print("Importing utils")
import extrautils
print("Importing commands")
import commands
print("Importing chatterbot")
import chatter

# create a new Client for the bot to run on.
print("magi-bot v0.1 starting up")
client = discord.Client()
# Open the file that contains the token for the bot.
token = extrautils.getCreds('creds.txt', 'token')
# don't mind me
swarm_id = "225804714141286401"
# read the profile picture into a variable
print("reading profile picture")
with open("magi093.png", 'rb') as f:
    profile = f.read()

# called when bot becomes ready for use
@client.event
async def on_ready():
    # set our profile picture
    print("setting profile picture")
    await client.edit_profile(avatar=profile)
    # print out a link to invite the bot to a server
    print('Logged in as ' + client.user.name)
    print('Id: ' + client.user.id)
    print("Invite link: " + discord.utils.oauth_url("168343655264944128"))

@client.event
async def on_message(message):
    mention = message.server.me.mention if message.server else bot.user.mention
    if message.content.startswith('?messagecount'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages, @'.format(counter) + message.author.name)
    # do nothing for 5 seconds. somehow the bot still runs commands whilst waiting
    elif message.content.startswith('?sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping.')
    # joke commands
    elif message.content.startswith('?robot'):
        await client.send_message(message.channel, 'BLEEP BLOOP')
    elif message.content.startswith('?bug'):
        await client.send_message(message.channel, "It's not a bug, it's a feature.")
    # Stop the bot
    elif message.content == '?cease':
        author = message.author
        authorname = author.id
        if authorname == '164342765394591744':
            await client.send_message(message.channel, 'Ceasing.')
            await client.logout()
        else:
            await client.send_message(message.channel, "Sorry, you don't have the ability to do that.")
    # repeat after the user
    elif message.content.startswith('?echo '):
        echo = message.content[6:]
        echoverify = message.content[6:12]
        # YES THE SPACE IS NECESARY
        if echoverify == '?echo ' or echoverify == '?echo' or echo == '':
            pass
        elif message.author.id != swarm_id and message.author.id != '169087865609912320':
            await client.send_message(message.channel, echo)
        else:
            pass
    # tts sh*tposting
    elif message.content =='?w':
        await client.send_message(message.channel, "wwwwwwwwwwwwwww", tts=True)
    elif message.content.startswith('?dramatic'):
        await client.send_message(message.channel, "dun\ndun\nduuuuuuuuuuun", tts=True)

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
    elif message.content.startswith("?invite"):
        invite_id = message.content[8:]
        if invite_id == "":
            await commands.invite(client, message)
        else:
            await commands.invite(client, message, invite_id)
    # find and delete messages which contain wildbot or aethex voice commands
    # get a music channel you twits
    elif commands.check_message_for_wildbot(message) or commands.check_message_for_aethex(message):
        print(message.author.name + " tried to call a music bot in #" + message.channel.name + ".")
        warnmsg = await client.send_message(message.channel, "Please do not [ACTION:POST] [ABSTRACT:THEMES] [LOCATION:HERE]. [ENTITY:HITLERMOD] does not [ACTION:LIKE] that.")
        try:
            await client.delete_message(message)
        except discord.errors.Forbidden:
            await client.send_message(message.channel, "Please give the bot the permission to delete messages to use this feature.")
        await asyncio.sleep(5)
        await client.delete_message(warnmsg)

    # ChatBot!
    # TODO: upgrade chatterbot to allow using mychatbot.recent_statements.flush()
    # thanks @gunthercox
    elif message.content == "?resetchatter":
        if message.server.id == "225619147046780930":
            chatter.candybot.recent_statements.queue = []
        elif message.server.id == "81384788765712384":
            chatter.api_memer.recent_statements.queue = []
        await client.send_message(message.channel, "Conversation cleared.")
    # send the message to the actual chatterbot
    elif message.content.startswith(mention) and message.author.id != "169087865609912320":
        message_minus_mention = message.content[len(mention)+1:]
        if message_minus_mention == "say hello" or message_minus_mention == "Say hello":
            await client.send_message(message.channel, "Hello!")
        elif message_minus_mention == "say goodbye" or message_minus_mention == "Say goodbye":
            await client.send_message(message.channel, "Farewell!")
        elif message_minus_mention.startswith("say hello to ") or message_minus_mention.startswith("Say hello to "):
            await client.send_message(message.channel, "Hello " + message_minus_mention[13:])
        elif message_minus_mention.startswith("say goodbye to ") or message_minus_mention.startswith("Say goodbye to "):
            await client.send_message(message.channel, "Goodbye " + message_minus_mention[15:])
        else:
            await client.send_typing(message.channel)
            # worldproblems server
            if message.server.id == "225619147046780930" and message.author.id != swarm_id:
                candy_speaks = chatter.talk_to_the_dead(message.content[len(mention) + 1:])
                await client.send_message(message.channel, candy_speaks)
            # discord API server
            elif message.server.id == "81384788765712384":
                mr_wumpus = chatter.may_i_speak_to_the_wumpus(message.content[len(mention) + 1:])
                await client.send_message(message.channel, mr_wumpus)
            elif message.author.id == swarm_id:
                pass
            else:
                await client.send_message(message.channel, "Your server doesn't have a chatterbot configured for it yet!\nGo pester @tkdberger on GitHub to get this fixed!")

client.run(token)
