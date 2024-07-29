import pandas as pd

fielding_df = pd.read_csv('data/csvs/Fielding.csv')

names = pd.read_csv('data/csvs/Names.csv')

# filter the data to include only data from 2012
filtered_df = fielding_df[fielding_df['yearID'] == 2012]

# filter the data to include fielders who have played in 100 games or more
filtered_df = filtered_df[filtered_df['G'] >= 100]

# calculate fielding percentage, round to 3 decimal places
filtered_df['FieldingPct'] = (filtered_df['PO'] + filtered_df['A']) / (filtered_df['PO'] +
                                                                       filtered_df['A'] +
                                                                       filtered_df['E'])
filtered_df['FieldingPct'] = filtered_df['FieldingPct'].round(3)

filtered_df = filtered_df.dropna(subset=['FieldingPct']) # filter out any rows that have NA for FieldingPct

max_row = filtered_df.loc[filtered_df['FieldingPct'].idxmax()] # line that returns the player with the highest fielding percentage
# print(max_row)

# calculate stolen base percentage for catchers, round to 3 decimal places
filtered_df['CatcherStealPct'] = filtered_df['CS'] / (filtered_df['SB'] +
                                                      filtered_df['CS'])

filtered_df['CatcherStealPct'] = filtered_df['CatcherStealPct'].round(3)

filtered_df = pd.merge(filtered_df, names, on='playerID', how='left')

# export df with fielding percentage and catcher stolen base percent
filtered_df.to_csv('2012_Fielders.csv', index=False)