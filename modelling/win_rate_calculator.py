import json
import pandas as pd

REQUIRED_RECORD_ROWS = ['match_id', 'hero_id', 'player_slot', 'radiant_win']
HERO_WIN_RATE = {}


def main():
    players = pd.read_csv('data/players.csv')
    matches = pd.read_csv('data/match.csv')

    merged_player_records = pd.merge(left=players, right=matches, how='inner', on='match_id')[REQUIRED_RECORD_ROWS]
    merged_player_records.apply(add_data_to_winrate, axis=1)

    hero_win_out = {}
    for hero_id, values in HERO_WIN_RATE.items():
        win_rate = float(values['num_wins']) / float(values['num_games'])
        hero_win_out[hero_id] = win_rate

    with open('data/hero_win_rate.json', 'w') as file:
        json.dump(hero_win_out, file)

    print('Hero win rates dumped successfully!')


def add_data_to_winrate(panda_row):
    hero_id = panda_row['hero_id']
    player_slot = panda_row['player_slot']
    radiant_win = panda_row['radiant_win']

    if str(hero_id) == '0':
        return

    if hero_id in HERO_WIN_RATE:
        HERO_WIN_RATE[hero_id]['num_games'] += 1
    else:
        HERO_WIN_RATE[hero_id] = {'num_wins': 0, 'num_games': 1}

    if player_slot <= 4 and radiant_win:
        HERO_WIN_RATE[hero_id]['num_wins'] += 1
    elif player_slot >= 4 and not radiant_win:
        HERO_WIN_RATE[hero_id]['num_wins'] += 1


if __name__ == '__main__':
    main()
