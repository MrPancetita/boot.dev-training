# https://www.boot.dev/lessons/ff46b302-8371-4c3e-9dcd-3b306575ea02

def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}"
    }

