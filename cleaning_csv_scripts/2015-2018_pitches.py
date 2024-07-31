import pandas as pd

# Each row is an indvidual pitch
pitches = pd.read_csv('data/raw_csvs/pitches.csv')

pitcher_names = pd.read_csv('data/raw_csvs/pitch_data_names.csv')

at_bats = pd.read_csv('data/raw_csvs/atbats.csv')

# change id in pitcher_names to pitcher_id
at_bats.rename(columns={'pitcher_id': 'id'}, inplace=True)

# Merge at_bats with pitch_data_names to get pitcher and batter names
merged_ab = at_bats.merge(pitcher_names, on='id', how='left')

# Merge with pitches to get pitch details
final_df = merged_ab.merge(pitches, on='ab_id', how='left')

final_df = final_df[['PlayerName', 'code', 'pitch_type', 'spin_rate', 'start_speed', 'stand', 'p_throws', 'event', 'ab_id']]

# print(final_df.columns)
# print(final_df.head())

final_df.to_csv('ml_pitches.csv', index=False)