import json
import pickle

import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


REQUIRED_RECORD_ROWS = ['match_id', 'hero_id', 'player_slot', 'radiant_win']
HERO_WIN_RATES = json.load(open('data/hero_win_rate.json', 'r'))


def main():
    players = pd.read_csv('data/players.csv')
    matches = pd.read_csv('data/match.csv')

    merged_player_records = pd.merge(left=players, right=matches, how='inner', on='match_id')[REQUIRED_RECORD_ROWS]
    features = merged_player_records.groupby('match_id').agg({'hero_id': lambda x: list(x), 'radiant_win': 'first'})
    features['ordered_wr'] = features['hero_id'].apply(prepare_win_rate_features)

    x = np.array(features['ordered_wr'].values.tolist())
    y = np.array(features['radiant_win'].values.astype('int').tolist())

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)

    logistic_reg = LogisticRegression()

    trained_model = logistic_reg.fit(x_train, y_train)
    joblib.dump(trained_model, 'logistic_model.pkl')


def prepare_win_rate_features(row):
    radiant_heroes, dire_heroes = row[:5], row[5:]

    radiant_win_rates = [_get_win_rate_hero(hero_id) for hero_id in radiant_heroes]
    dire_win_rates = [_get_win_rate_hero(hero_id) for hero_id in dire_heroes]

    ordered_radiant_win_rates = sorted(radiant_win_rates, reverse=True)
    ordered_dire_win_rates = sorted(dire_win_rates, reverse=True)

    return ordered_radiant_win_rates + ordered_dire_win_rates


def _get_win_rate_hero(hero_id):
    try:
        return HERO_WIN_RATES[str(hero_id)]
    except KeyError:
        return 0.50


if __name__ == '__main__':
    main()
