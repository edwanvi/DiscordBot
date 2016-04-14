# import discord
import json

class CustomUser:
    def __init__(self, name, isBot, source):
        self.name = name
        if isBot == "True":
            self.isBot = True
        else:
            self.isBot = False

        self.source = source


def readTheJson(filename):
    # read it
    with open(filename) as data_file:
        data = json.load(data_file)
        print(data)


sources = {'self': 'tkdberger/DiscordBot', 'rdanny': 'Rapptz/RoboDanny'}
print(sources['self'] + ' so https://www.github.com/' + sources['self'])
print(sources['rdanny'])
readTheJson('data.json')
