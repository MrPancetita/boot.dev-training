# https://www.boot.dev/lessons/8b3ac017-64fd-463f-991d-aecf380c6f71

def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",
    }
