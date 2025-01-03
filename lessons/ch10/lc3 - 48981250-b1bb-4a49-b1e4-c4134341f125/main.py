# https://www.boot.dev/lessons/48981250-b1bb-4a49-b1e4-c4134341f125

def calculate_total(items_purchased, pinned_list):
    item_prices = {
        "health_potion": 10.00,
        "mana_potion": 12.00,
        "gold_dust": 5.00,
        "dwarven_ale": 8.00,
        "enchanted_scroll": 25.00,
        "ice_cold_milk": 50.00,
        "herbs": 7.00,
        "crystal_shard": 20.00,
        "magic_ring": 100.00,
        "mystic_amulet": 150.00,
    }

    # Don't touch above this line

    unpurchased_items = []
    receipt = {}

    for item in pinned_list:
        if item not in items_purchased:
            unpurchased_items.append(item)

    for item in items_purchased:
        receipt[item] = item_prices[item]
    
    total = sum(receipt.values())

    return unpurchased_items, receipt, total
