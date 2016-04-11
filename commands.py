"""
The commands that aren't in main.py.
I hope i can get this to work.
"""
# Import the needed modules.
import extrautils

# create a new Client for the bot to run on.
# Open the file that contains the username and password for the account.
username = extrautils.getCreds('creds.txt', 'username')
password = extrautils.getCreds('creds.txt', 'password')

helptext = " \n".join(
        [
            "`?help`: this text\n"
            "`?test`: See how many times the bot has seen you speak\n"
            "`?robot`: BLEEP BLOOP\n"
            "`?echo`: have the robot repeat you\n"
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
    git_url = '''https://www.github.com/''' + git_user_name
    git_pages = '''https://{}.github.io'''.format(git_user_name)
    await client.send_message(message.channel, 'Github User page: ' + git_url)
    await client.send_message(message.channel, 'Github Pages site: ' + git_pages)