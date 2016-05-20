# import discord
import json


def readTheJson(filename):
    # read it
    with open(filename) as data_file:
        data = json.load(data_file)
        print(data)
        print(data["magi-bot"])


sources = {'self': 'tkdberger/DiscordBot', 'rdanny': 'Rapptz/RoboDanny'}
print(sources['self'] + ' so https://www.github.com/' + sources['self'])
print(sources['rdanny'])
readTheJson('data.json')

