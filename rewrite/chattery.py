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
        "chatterbot.logic.TimeLogicAdapter",
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
        pass
