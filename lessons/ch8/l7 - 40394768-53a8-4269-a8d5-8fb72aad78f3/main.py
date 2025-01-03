# https://www.boot.dev/lessons/40394768-53a8-4269-a8d5-8fb72aad78f3

def count_down(start, end):
    for i in range(start, end, -1):
        print(i)


# Don't edit below this line


def test(start, end):
    print(f"Using inputs start: {start} and end: {end}")
    print(f"Printing numbers from {start} to {end + 1}:")
    count_down(start, end)
    print("=====================================")


def main():
    test(10, 0)
    test(20, 10)
    test(15, 11)


main()