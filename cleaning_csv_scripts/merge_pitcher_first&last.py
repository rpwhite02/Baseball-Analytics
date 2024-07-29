import pandas as pd

pitcher_names = pd.read_csv('data/csvs/pitch_data_names.csv')

pitcher_names['PlayerName'] = pitcher_names['first_name'] + ' ' + pitcher_names['last_name']

# drop individual first and last name columns
player_names = pitcher_names.drop(columns=['first_name', 'last_name'])

# pitch_data_names now only has pitcher id and pitcher names (in one column)
player_names.to_csv('pitch_data_names.csv', index=False)