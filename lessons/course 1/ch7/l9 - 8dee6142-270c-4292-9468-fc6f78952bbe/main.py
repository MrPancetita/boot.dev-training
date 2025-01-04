# https://www.boot.dev/lessons/8dee6142-270c-4292-9468-fc6f78952bbe

def does_attack_hit(attack_roll, armor_class):
    return (attack_roll != 1 and attack_roll >= armor_class) or attack_roll == 20

