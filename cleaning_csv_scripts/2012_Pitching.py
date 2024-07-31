import pandas as pd

pitching_df = pd.read_csv('data/raw_csvs/Pitching.csv')

names = pd.read_csv('data/raw_csvs/Names.csv')

# calculate innings pitched because outs pitched is fucking stupid idk why they did that
pitching_df['IP'] = pitching_df['IPouts'] / 3

# include only the year 2012
filtered_df = pitching_df[pitching_df['yearID'] == 2012]

# include only pitchers with 30 IP with ONE TEAM
filtered_df = filtered_df[filtered_df['IP'] >= 30]
filtered_df['IP'] = filtered_df['IP'].round(2)

# calculate WHIP without IBB
filtered_df['WHIP'] = (filtered_df['H'] + filtered_df['BB']) / filtered_df['IP']
filtered_df['WHIP'] = filtered_df['WHIP'].round(2)

# calculate K/9
filtered_df['K/9'] = (filtered_df['SO'] * 9) / filtered_df['IP']
filtered_df['K/9'] = filtered_df['K/9'].round(2)

# calculate BB/9
filtered_df['BB/9'] = (filtered_df['BB'] * 9) / filtered_df['IP']
filtered_df['BB/9'] = filtered_df['BB/9'].round(2)

# calculate HR/9
filtered_df['HR/9'] = (filtered_df['HR'] * 9) / filtered_df['IP']
filtered_df['HR/9'] = filtered_df['HR/9'].round(2)

# calculate K percentage
filtered_df['KPct'] = (filtered_df['SO'] / filtered_df['BFP']) * 100
filtered_df['KPct'] = filtered_df['KPct'].round(2)

filtered_df = pd.merge(filtered_df, names, on='playerID', how='left')

# assign player name column to move to front of dataframe 
column_to_move = filtered_df.pop('PlayerName')

# Insert the column at the first position
filtered_df.insert(0, 'PlayerName', column_to_move)

# remove playerID
filtered_df.pop('playerID')

filtered_df.to_csv('2012_Pitchers.csv', index=False)

# separate pitchers into relievers and starters based on innings and games started

relievers = filtered_df[(filtered_df['IP'] <= 80 ) & (filtered_df['G'] > 10)]

starters = filtered_df[(filtered_df['IP'] >= 100) & (filtered_df['GS'] > 15)]

relievers.to_csv('2012_Relievers.csv', index=False)

starters.to_csv('2012_Starters.csv', index=False)