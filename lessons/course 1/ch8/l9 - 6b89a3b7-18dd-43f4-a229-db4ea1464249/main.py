#https://www.boot.dev/lessons/6b89a3b7-18dd-43f4-a229-db4ea1464249

def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total
