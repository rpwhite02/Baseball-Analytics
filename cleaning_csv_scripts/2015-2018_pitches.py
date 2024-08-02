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

final_df = final_df[['PlayerName', 'break_angle', 'break_length', 'code', 'nasty', 'pitch_num', 'pitch_type', 'spin_dir',
                     'spin_rate', 'start_speed', 'type', 'x', 'y', 'stand']]

# Change batter stance from L and R to left and right
final_df['stand'] = final_df['stand'].replace({'L': 'left', 'R': 'right'})

# Filter the dataframe to only include specific pitchers
verlander = final_df[final_df['PlayerName'] == 'Justin Verlander']

# Create separate dataframes for each of the pitcher's pitch types and export to CSV
changeups = verlander[verlander['pitch_type'] == 'CH']
changeups.to_csv('data/pitcher_csvs/verlander_pitches/verlander_FF.csv', index=False)

curveballs = verlander[verlander['pitch_type'] == 'CU']
curveballs.to_csv('data/pitcher_csvs/verlander_pitches/verlander_CU.csv', index=False)

cutters = verlander[verlander['pitch_type'] == 'FC']
cutters.to_csv('data/pitcher_csvs/verlander_pitches/verlander_FC.csv', index=False)

fastballs = verlander[verlander['pitch_type'] == 'FF']
fastballs.to_csv('data/pitcher_csvs/verlander_pitches/verlander_FF.csv', index=False)

twoseams = verlander[verlander['pitch_type'] == 'FT']
twoseams.to_csv('data/pitcher_csvs/verlander_pitches/verlander_FT.csv', index=False)

sliders = verlander[verlander['pitch_type'] == 'SL']
sliders.to_csv('data/pitcher_csvs/verlander_pitches/verlander_SL.csv', index=False)