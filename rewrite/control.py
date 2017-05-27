"""
Commands for bot control (shut down and what not.)
"""
import discord
from discord.ext import commands

class Admin():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Stops the bot if you have the power to do so (ya don't)", pass_context=True)
    async def cease(self, ctx):
        """Stops the robot."""
        member = ctx.message.author
        if member.id == '164342765394591744':
            await self.bot.say("Ceasing.")
            await self.bot.logout()

def setup(bot):
    bot.add_cog(Admin(bot))
