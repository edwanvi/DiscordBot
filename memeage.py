import discord
from discord.ext import commands

class memeage():
    def __init__(self, bot):
        self.bot = bot
        buddy = open('./buddy.txt')
        """
        The hey there buddy copypasta as a single string.
        Because I hate you all.
        """
        self.buddytxt = buddy.read()
        buddy.close()

    @commands.command()
    async def heythere(self):
        """hey there buddy"""
        await self.bot.say(self.buddytxt)

def setup(bot):
    bot.add_cog(memeage(bot))
