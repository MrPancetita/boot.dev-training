# https://www.boot.dev/lessons/6e61347c-ff5e-453b-a35f-680e2775c0e3

def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    else:
        return "neither"

