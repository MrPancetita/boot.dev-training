# https://www.boot.dev/lessons/de1acdfc-4aca-4c12-ae73-c6bbcf92dc66

def get_most_common_enemy(enemies_dict):
    most_common_enemy = None
    max_so_far = float("-inf")
    for enemy in enemies_dict:
        if enemies_dict[enemy] > max_so_far:
            most_common_enemy = enemy
            max_so_far = enemies_dict[enemy]
    return most_common_enemy


