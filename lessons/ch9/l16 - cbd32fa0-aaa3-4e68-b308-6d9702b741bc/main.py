# https://www.boot.dev/lessons/cbd32fa0-aaa3-4e68-b308-6d9702b741bc

def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        if i % 2 != 0:
            odd_numbers.append(i)
    # don't touch below this line

    return odd_numbers

