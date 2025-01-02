# https://www.boot.dev/lessons/50c2ae9b-a4e5-45ca-b462-9e91911d993c

def is_prime(number):
    if number < 2:
        return False
    for i in range (2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

