# https://www.boot.dev/lessons/a5e9b2de-7530-413b-a86c-60afacf54fa9

def find_missing_ids(first_ids, second_ids):
    return list(set(first_ids).difference(second_ids))
