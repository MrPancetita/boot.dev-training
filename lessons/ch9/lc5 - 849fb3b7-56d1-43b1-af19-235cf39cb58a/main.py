# https://www.boot.dev/lessons/849fb3b7-56d1-43b1-af19-235cf39cb58a

def double_string(string):
    doubled_string = []
    for char in string:
        doubled_string.append(char * 2)
    return "".join(doubled_string)
