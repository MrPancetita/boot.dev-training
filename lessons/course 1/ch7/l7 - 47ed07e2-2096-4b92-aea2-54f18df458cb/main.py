# https://www.boot.dev/lessons/47ed07e2-2096-4b92-aea2-54f18df458cb

def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"