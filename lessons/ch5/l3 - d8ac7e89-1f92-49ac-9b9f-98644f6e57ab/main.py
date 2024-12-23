# https://www.boot.dev/lessons/d8ac7e89-1f92-49ac-9b9f-98644f6e57ab

def take_magic_damage(health, resist, amp, spell_power):
    damage = spell_power * amp - resist
    health -= damage
    return health