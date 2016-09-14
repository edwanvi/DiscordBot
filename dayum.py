# import discord
import json
gitxt = ' so https://www.github.com/'

def readTheJson(filename):
    # read it
    with open(filename) as data_file:
        data = json.load(data_file)
        #print(data) <- just don't
        print(data["magi-bot"])

sources = {'self': 'tkdberger/DiscordBot', 'rdanny': 'Rapptz/RoboDanny'}
print(sources['self'] + ' so https://www.github.com/' + sources['self'])
print(sources['rdanny'] + gitxt + sources['rdanny'])
readTheJson('data.json')
