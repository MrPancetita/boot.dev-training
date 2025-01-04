# https://www.boot.dev/lessons/1cf6ca96-28e4-4788-a103-d442a42056d8

def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line

    for i in range(0, len(items)):
        if items[i] == "Potion":
            potion_count += 1
        elif items[i] == "Bread":
            bread_count += 1
        elif items[i] == "Shortsword":
            shortsword_count += 1
    # don't touch below this line

    return potion_count, bread_count, shortsword_count