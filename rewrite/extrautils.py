def getCreds(filename, cred):
    """
    Open the file that contains the username and password for the account and return the specified credential.
    works remarkably well for a piece of code I wrote.
    """
    username, password, token = (None, None, None)
    datafile = open(filename)
    username = None
    password = None
    token = None
    for line in datafile:
        if line.startswith('u:') and username == None:
            username = line[2:]
            username = username.rstrip()
        elif line.startswith('p:') and password == None:
            password = line[2:]
            password = password.rstrip()
        elif line.startswith('t:') and token == None:
            token = line[2:]
            token = token.rstrip()
        else:
            print("Input file not valid. Terminating.")
            pass
    if cred == 'username':
        return username
    elif cred == 'password':
        return password
    elif cred == 'token':
        return token