# https://www.boot.dev/lessons/7ad74b3d-cde8-4d03-a548-0326b0e0fda8

def join_strings(strings):
    final_string = ""
    for string in strings:
        final_string += string + ","
    return final_string[:-1]
