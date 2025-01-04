# https://www.boot.dev/lessons/5d1f57f0-bed4-4db9-8881-089376508b52

def purchase_item(price, gold_available):
    if gold_available >= price:
        return gold_available - price
    else:
        raise Exception("not enough gold")
