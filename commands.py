"""
The commands that aren't in main.py.
I hope i can get this to work.
"""
# Import the needed modules.
import discord
import asyncio
import extrautils

# create a new Client for the bot to run on.
# Open the file that contains the username and password for the account.
username = extrautils.getCreds('creds.txt', 'username')
password = extrautils.getCreds('creds.txt', 'password')


async def send_help(client, message):
    print("function was called")
    await client.send_message(message.channel, "Sorry, you don't have the ability to do that.")
