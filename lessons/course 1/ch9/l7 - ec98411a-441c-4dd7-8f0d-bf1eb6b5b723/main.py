# https://www.boot.dev/lessons/ec98411a-441c-4dd7-8f0d-bf1eb6b5b723

def smelt_ore(inventory):
    if inventory[1] == "Iron Ore":
        inventory[1] = "Iron Bar"
    return inventory
