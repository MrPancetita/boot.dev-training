# https://www.boot.dev/lessons/565dd496-0765-4e10-b074-85931fba340f

def calculate_experience_points(level):
    experience_points = 0
    for i in range(1, level):
        experience_points += 5 * i
    return experience_points

