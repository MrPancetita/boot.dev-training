# https://www.boot.dev/lessons/3af04a3f-12e4-444f-b2a7-4060b8e35fad

def player_status(health):
    if health <= 0:
        return "dead"
    elif health <= 5:
        return "injured"
    return "healthy"

