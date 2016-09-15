# import discord
import json

datafile = 'json_testland.json'

class test_user(object):
    """
    docstring for test_user.
    """
    def __init__(self, name, nickname, userid):
        super(test_user, self).__init__()
        self.name = name
        self.nickname = nickname
        self.id = userid

with open(datafile, mode='w', encoding='utf-8') as f:
    json.dump([], f)

def add_to_json(filename, args):
    with open(filename, mode='r', encoding='utf-8') as feedsjson:
        feeds = json.load(feedsjson)

    with open(filename, mode='w', encoding='utf-8') as feedsjson:
        entry = {'name': args.name, 'nickname': args.nickname, 'id': args.id}
        feeds.append(entry)
        json.dump(feeds, feedsjson, sort_keys=True, indent=4)
