# https://www.boot.dev/lessons/9c7d3a68-9e06-48a6-86d1-2ea462cfc256

def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance > 3:
        current_health += 1
        enemy_distance -= 2
    return current_health