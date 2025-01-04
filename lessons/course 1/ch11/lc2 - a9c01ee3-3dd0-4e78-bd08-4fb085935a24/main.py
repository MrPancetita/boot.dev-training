# https://www.boot.dev/lessons/a9c01ee3-3dd0-4e78-bd08-4fb085935a24

def count_vowels(text):
    vowels = {"a","e","i","o","u","A","E","I","O","U"}
    used_vowels = vowels.intersection(set(text)) 
    occurrences = 0

    for letter in text:
        if letter in used_vowels:
            occurrences += 1

    return occurrences, used_vowels


