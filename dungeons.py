import discord
import json
import math
import random
from discord.ext import commands

scores = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

class dungeons():
    def __init__(self, bot):
        self.bot = bot
        with open('./dungeon.json') as dungeon: 
            self.raw_db = json.load(dungeon)

    @commands.command()
    async def dump_db(self):
        """DEBUG - dumps the entire character database if it fits in a single message."""
        await self.bot.say(self.raw_db)

    @commands.command(pass_context=True, description="Looks up your D&D character or reports your lack of one.")
    async def get_char(self, ctx):
        author = ctx.message.author
        id = author.id
        try:
            character_dict = self.raw_db[id]
            em = discord.Embed(title=character_dict["name"], colour=author.colour)
            em.set_footer(text=self.bot.user.name, icon_url="http://i.imgur.com/hSLoK3k.png")
            try:
                em.set_thumbnail(url=character_dict["thumbnail"])
            except KeyError as e:
                print("No thumbnail, continuing without it")
            # scores = ["strength", "intelligence", "wisdom", "charisma", "constitution", "dexterity"]
            for val in scores:
                score = character_dict[val]
                modifier = get_modifier(score)
                if modifier >= 0:
                    final = "{} (+{})".format(str(score), str(modifier))
                else:
                    final = "{} ({})".format(str(score), str(modifier))
                em.add_field(name=val.title(), value=final, inline=False)
            em.add_field(name="Age", value=character_dict["age"], inline=True)
            em.add_field(name="Race", value=character_dict["race"], inline=True)
            em.add_field(name="Class", value=character_dict["class"], inline=True)
            await self.bot.send_message(ctx.message.channel, None, tts=False, embed=em)
        except KeyError as e:
            print(e)
            await self.bot.say("You don't have a character configured yet!")

    @commands.command(pass_context=True, description="Looks up someone else's D&D character or reports thier lack of one.")
    async def steal_char(self, ctx, *, id: str):
        author = ctx.message.author
        try:
            character_dict = self.raw_db[id]
            em = discord.Embed(title=character_dict["name"], colour=author.colour)
            em.set_footer(text=self.bot.user.name, icon_url="http://i.imgur.com/hSLoK3k.png")
            try:
                em.set_thumbnail(url=character_dict["thumbnail"])
            except KeyError as e:
                print("No thumbnail, continuing without it")
            # scores = ["strength", "intelligence", "wisdom", "charisma", "constitution", "dexterity"]
            for val in scores:
                score = character_dict[val]
                modifier = get_modifier(score)
                if modifier >= 0:
                    final = "{} (+{})".format(str(score), str(modifier))
                else:
                    final = "{} ({})".format(str(score), str(modifier))
                em.add_field(name=val.title(), value=final, inline=False)
            em.add_field(name="Age", value=character_dict["age"], inline=True)
            em.add_field(name="Race", value=character_dict["race"], inline=True)
            em.add_field(name="Class", value=character_dict["class"], inline=True)
            await self.bot.send_message(ctx.message.channel, None, tts=False, embed=em)
        except KeyError as e:
            print(e)
            await self.bot.say("They don't have a character configured yet!")


    @commands.command(description="Rolls 1d20 plus the selected modifier.", pass_context=True)
    async def check(self, ctx, *, skill: str):
        author = ctx.message.author
        id = author.id
        character_dict = None
        try:
            character_dict = self.raw_db[id]
        except KeyError as e:
            await self.bot.say("You don't have a character configured yet!")
            return
        score = character_dict[skill]
        modifier = get_modifier(score)
        roll = random.randint(1, 20)
        final = ""
        if (modifier >= 0):
            final = "{} + {} = **{}**".format(str(roll), str(modifier), str(roll+modifier))
        else:
            final = "{} - {} = **{}**".format(str(roll), str(modifier), str(roll+modifier))
        await self.bot.say(final)

def setup(bot):
    bot.add_cog(dungeons(bot)) 

def get_modifier(score):
    return math.floor((score - 10)/2)

