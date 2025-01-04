# https://www.boot.dev/lessons/fc18fe71-7d0d-4883-9197-1040085af1fb

def get_champion_slices(champions):
    champions_list1 = champions[2:]
    champions_list2 = champions[0:-2]
    champions_list3 = champions[0::2]
    return champions_list1, champions_list2, champions_list3