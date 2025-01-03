# https://www.boot.dev/lessons/cfe23336-62b4-4f37-8e41-f1d2a24444fc

def get_odds_and_evens(numbers):
    num_odds = 0
    num_evens = 0

    # Don't touch above this line

    for number in numbers:
        if number % 2 == 0:
            num_evens += 1
        else:
            num_odds += 1
    
    return num_odds, num_evens
