# https://www.boot.dev/lessons/c36e1160-2b7f-49bd-96a1-4c8996e8c7d5

def validate_path(expected_path, character_path):
    character_name = character_path[0]
    character_wpts = character_path[1:]
    incorrect_wpts_count = 0
    for i in range (0, len(expected_path)):
        if expected_path[i] != character_wpts[i]:
            incorrect_wpts_count += 1

    accuracy = (len(expected_path) - incorrect_wpts_count) / len(expected_path) * 100
    return (character_name, accuracy)