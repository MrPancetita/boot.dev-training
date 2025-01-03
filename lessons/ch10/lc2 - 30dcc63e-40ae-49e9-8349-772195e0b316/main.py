# https://www.boot.dev/lessons/30dcc63e-40ae-49e9-8349-772195e0b316

def merge(dict1, dict2):
    for key in dict2:
        dict1[key] = dict2[key]
    return dict1
       
def total_score(score_dict):
    total = 0
    for key in score_dict:
        total += score_dict[key]
    return total
