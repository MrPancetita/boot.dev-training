# https://www.boot.dev/lessons/d91979cc-c760-4dec-aff8-cbe25b0ea505

def meditate(mana, max_mana, energy, energy_drinks):
    while mana < max_mana and (energy > 0 or energy_drinks > 0):
        if energy > 0:
            energy -= 1
            mana += 1
        else:
            energy_drinks -= 1
            energy += 50
    return mana, energy, energy_drinks 
        
    
