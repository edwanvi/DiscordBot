"""
Rewritten chatterbot class.
"""
import discord
from discord.ext import commands
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

print("Reviving the dead...")
candybot = ChatBot("CandyToast",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    database="../candy_toast.json",
    silence_performance_warning=True,
#    filters=["chatterbot.filters.RepetitiveResponseFilter"]
)

class Chatter():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Allows you to talk to the dead. Only works if you happen to be in the right spot.", pass_context=True)
    async def speak(self, ctx, *, message: str):
        """Talks to the spirit of CandyToast, using SCP-████."""
        if ctx.message.server.id == "225619147046780930":
            print("user said: " + message)
            await self.bot.send_typing(ctx.message.channel)
            candy_speaks = candybot.get_response(message)
            print("bot said: " + candy_speaks.text)
            await self.bot.say(candy_speaks)
    @commands.command(description="Purges the CandyToast conversation.", pass_context=True)
    async def reset_chatter(self, ctx):
        """Purges the CandyToast conversation."""
        if ctx.message.server.id == "225619147046780930":
            # get session
            session = candybot.default_session
            session.conversation.flush()
            await self.bot.say("conversation cleared")
        else:
            pass

def setup(bot):
    bot.add_cog(Chatter(bot))
