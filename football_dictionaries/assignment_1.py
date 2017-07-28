def players_as_dictionaries(squads_list):
    squad_as_dict = []
    for player in squads_list:
        player_dict = {
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8],
        }
        squad_as_dict.append(player_dict)
    return squad_as_dict


if __name__ == '__main__':
    from squads_data import SQUADS_DATA
    squad_dict = players_as_dictionaries(SQUADS_DATA)
    import ipdb; ipdb.set_trace()
