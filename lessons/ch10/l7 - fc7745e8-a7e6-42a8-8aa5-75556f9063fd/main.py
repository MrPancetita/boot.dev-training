# https://www.boot.dev/lessons/fc7745e8-a7e6-42a8-8aa5-75556f9063fd

def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name in enemies_dict:
            enemies_dict[enemy_name] += 1
        else:
            enemies_dict[enemy_name] = 1
    return enemies_dict
