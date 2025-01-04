# https://www.boot.dev/lessons/eb147649-719f-4946-8edd-a8ee5578b9fd

def contains_leather_scraps(items):
    found = False

    # don't touch above this line

    for item in items:
        if item == "Leather Scraps":
            found = True
            break

    # don't touch below this line

    return found