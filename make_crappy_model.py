import json
import pandas as pd
import sklearn

REQUIRED_RECORD_ROWS = ['match_id', 'hero_id', 'player_slot', 'radiant_win']
HERO_WIN_RATES = json.load(open('Dota2_data/hero_win_rate.json'))


def main():
    players = pd.read_csv('Dota2_data/players.csv')
    matches = pd.read_csv('Dota2_data/match.csv')
    merged_player_records = pd.merge(left=players, right=matches, how='inner', on='match_id')[REQUIRED_RECORD_ROWS]
    test_df = merged_player_records.groupby('match_id').agg({'hero_id': lambda x: list(x), 'radiant_win': 'first'})
    return


if __name__ == '__main__':
    main()
