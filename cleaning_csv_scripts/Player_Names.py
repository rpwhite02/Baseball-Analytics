import pandas as pd

player_names = pd.read_csv('data/raw_csvs/Master.csv', usecols=['playerID', 'nameFirst', 'nameLast'])

# combine first and last name into one column
player_names['PlayerName'] = player_names['nameFirst'] + ' ' + player_names['nameLast']

# drop individual first and last name columns
player_names = player_names.drop(columns=['nameFirst', 'nameLast'])

player_names.to_csv('Names.csv', index=False)