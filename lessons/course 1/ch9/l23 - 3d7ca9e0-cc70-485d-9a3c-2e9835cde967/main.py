# https://www.boot.dev/lessons/3d7ca9e0-cc70-485d-9a3c-2e9835cde967

def reverse_array(items):
    reversed_array = []
    for i in range(len(items), 0, -1):
        reversed_array.append(items[i-1])
    return reversed_array

