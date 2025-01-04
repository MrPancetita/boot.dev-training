# https://www.boot.dev/lessons/d6a705f8-7d2b-4be5-aa38-6bad6c5eabb7

def countdown_to_start():
    for i in range(10, 1, -1):
        print(f"{i}...")
    print("1...Fight!")

# Don't edit below this line


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()


