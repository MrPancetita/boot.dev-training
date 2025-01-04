# https://www.boot.dev/lessons/ff1b4f58-af4b-40ed-94dd-b83ce0a57279

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)
