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
    print("function was called by " + message.author.name)
    await client.send_message(message.channel, "Oh did you want some help? \n" + helptext)
