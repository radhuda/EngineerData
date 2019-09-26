molecule = 'zinc'

def remove_white_spaces(string):
    string = string.split(' ')
    string = list(filter(None, string))
    if string[0] == 'M':
        if str(string[1:2])[2] == 'Z':
            global molecule
            molecule = str(string[1:2])[2:18]
            return (molecule , (string[0] , []))
        else:
            return (molecule, (string[0], string[1:]))
    else:
        return (molecule , (string[0], string[1:]))

