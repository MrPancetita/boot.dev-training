# https://www.boot.dev/lessons/e19e518e-8f06-4db8-942b-3c6aef880deb

def split_players_into_teams(players):
#    Shorter solution
#    even_team = players[::2]
#    odd_team = players[1::2]
    even_team = []
    odd_team = []
    for i in range(0, len(players)):
        if i % 2 == 0:
            even_team.append(players[i])
        else:
            odd_team.append(players[i])
    return even_team, odd_team


