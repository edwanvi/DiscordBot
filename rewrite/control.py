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
    
    @commands.command(description="Reloads a given extension.", pass_context=True)
    async def reload(self, ctx, *, extensionname: str):
        member = ctx.message.author
        message = extensionname
        if member.id == '164342765394591744':
            self.bot.unload_extension(message)
            self.bot.load_extension(message)
            self.bot.say("Reloaded " + message + " successfully.")

def setup(bot):
    bot.add_cog(Admin(bot))
