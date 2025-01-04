# https://www.boot.dev/lessons/0d2e3863-67f1-4cbd-bd7f-24536c140a26

def calculate_flurry_crit(num_attacks, base_damage):
    total_damage = 0
    for i in range (1, num_attacks):
        total_damage += base_damage * 2
    total_damage += base_damage * 4
    return total_damage


