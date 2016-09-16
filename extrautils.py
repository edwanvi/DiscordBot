import json
"""
Basically a stupid module of stupid functions for a stupid project.
Yeah.
"""

def getCreds(filename, cred):
    """Open the file that contains the username and password for the account."""
    datafile = open(filename)
    for line in datafile:
        if line.startswith('u:'):
            username = line[2:]
            username = username.rstrip()
        elif line.startswith('p:'):
            password = line[2:]
            password = password.rstrip()
        elif line.startswith('t:'):
            token = line[2:]
            token = token.rstrip()
        else:
            print("Input file not valid. Terminating.")
            exit()
    if cred == 'username':
        return username
    elif cred == 'password':
        return password
    elif cred == 'token':
        return token

datafile = "json_testland.json"

with open(datafile, mode='w', encoding='utf-8') as f:
    json.dump([], f)

def add_to_json(filename, args):
    with open(filename, mode='r', encoding='utf-8') as feedsjson:
        feeds = json.load(feedsjson)

    with open(filename, mode='w', encoding='utf-8') as feedsjson:
        entry = {'name': args.name, 'id': args.id, 'role': args.top_role.name}
        feeds.append(entry)
        json.dump(feeds, feedsjson, sort_keys=True, indent=4)
