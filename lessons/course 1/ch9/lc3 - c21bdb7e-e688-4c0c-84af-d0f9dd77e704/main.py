# https://www.boot.dev/lessons/c21bdb7e-e688-4c0c-84af-d0f9dd77e704

def check_ingredient_match(recipe, ingredients):
    missing_ingredients = []
    for i in range (0, len(recipe)):
        if recipe[i] != ingredients[i]:
            missing_ingredients.append(recipe[i])
    percentage = (len(recipe) - len(missing_ingredients)) / len(recipe) * 100  
    return percentage, missing_ingredients
