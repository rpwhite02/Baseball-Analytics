import pandas as pd

# Each row is an indvidual pitch
pitches = pd.read_csv('data/csvs/pitches.csv', usecols=['ab_id', 'event', 'pitcher_id', ''])
