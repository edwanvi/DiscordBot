"""
Basically a stupid module of stupid functions for a stupid project.
Yeah.
"""


def getCreds(filename, cred):
    # Open the file that contains the username and password for the account.
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
        else:
            print("Input file not valid. Terminating.")
            exit()
    if cred == 'username':
        return username
    elif cred == 'password':
        return password
    elif cred == 'token':
        return token