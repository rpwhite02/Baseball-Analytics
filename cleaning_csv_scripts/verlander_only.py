import pandas as pd

pitches = pd.read_csv('data/pitcher_csvs/2015-2018_pitches.csv')

jv = pitches['PlayerName'] == 'Justin Verlander'

verlander = pitches[jv]

verlander.to_csv('data/pitcher_csvs/verlander_only.csv')