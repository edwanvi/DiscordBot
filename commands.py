"""
The commands that aren't in main.py.
I hope i can get this to work.
"""
# Import the needed modules.
import extrautils
import asyncio
import json
import discord

# Open data.json for reading.
data_file = open('json_testland.json')
data = json.load(data_file)

helptext = " \n".join(
        [
            "`?help`: this text\n"
            "`?test`: See how many times the bot has seen you speak\n"
            "`?robot`: BLEEP BLOOP\n"
            "`?echo`: have the robot repeat you\n"
            "`?github <username>`: create and post the Github URLs for `username`.\n"
            "`?info <username>`: posts info on discord user `username`. If no such user is on record, the bot adds them.\n"
            "`?source`: Gets the bots source as it stands on Github.\n"
            "`?invite`: Prints the link to invite the bot to a server.\n"
            "Debug commands:\n"
            "`?cease`: stop the bot. Can only be executed by @magi093."
        ])

async def send_help(client, message):
    print("help was called by " + message.author.name)
    await client.send_message(message.channel, "Oh did you want some help? \n" + helptext)

async def hey_buddy(client, message):
    print('hey there ' + message.author.name + '...')
    # i have no regrets.
    await client.send_message(message.channel, '''hey there buddy chum pal friend buddy pal chum bud friend fella bruther amigo pal buddy friend chummy chum chum pal i don't mean to be rude my friend pal home slice bread slice dawg but i gotta warn ya if u take one more diddly darn step right there im going to have to diddly darn snap ur neck and wowza wouldn't that be a crummy juncture, huh? do you want that? do wish upon yourself to come into physical experience with a crummy juncture? because friend buddy chum friend chum pally pal chum friend if you keep this up well gosh diddly darn i just might have to get not so friendly with u my friendly friend friend pal friend buddy chum pally friend chum buddy...''')

async def github(client, message, git_user_name):
    print("Generating Git urls for " + git_user_name)
    git_url = '''https://www.github.com/''' + git_user_name
    git_pages = '''https://{}.github.io'''.format(git_user_name)
    await client.send_message(message.channel,
                              'Github User page: ' + git_url
                              + '\n' +
                              'Github Pages site: ' + git_pages
                              + '\n' +
                              'Note: both of these may 404, especially GitHub Pages.')

async def source(client, message):
    requestedSource = message.content[8:]
    if requestedSource == "":
        await client.send_message(message.channel, "https://www.github.com/tkdberger/DiscordBot")
    else:
        return

async def getUserInfo(client, message):
    user = message.content[6:]
    try:
        member = discord.utils.get(message.server.members, name=user)
        json_str = json.dumps({'name': member.name, 'id': member.id, 'role': member.top_role.name}, sort_keys=True, indent=4)
        if next((item for item in data if item["name"] == member.name), None) == None:
            print(message.author.name + " looked for found member(s) " + member.name)
            print(json_str)
            await client.send_message(message.channel, "```json\n" + json_str + "\n```")
            extrautils.add_to_json("json_testland.json", member)
        else:
            await client.send_message(message.channel, "```json\n" + json_str + "\n```")
    except AttributeError:
        print("Could not find specified user {}.".format(user))
        await client.send_message(message.channel, "Could not find specified user {}. Make sure to use their handle and not thier nickname.".format(user))

async def invite(client, message, id="168343655264944128"):
    await client.send_message(message.channel, "Invite link: " + discord.utils.oauth_url(id))
