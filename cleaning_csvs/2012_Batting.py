import pandas as pd

# import batting data
batting_df = pd.read_csv('data/csvs/Batting.csv')

names = pd.read_csv('data/csvs/Names.csv')

# filter the data to include only the year 2012
filtered_df = batting_df[batting_df['yearID'] == 2012]

# filter the data to include only players with 200 or more at bats
filtered_df = filtered_df[filtered_df['AB'] >= 200]

# calculate batting average and round to 3 decimal places
filtered_df['BattingAvg'] = filtered_df['H'] / filtered_df['AB']
filtered_df['BattingAvg'] = filtered_df['BattingAvg'].round(3)

# calculate OBP and round to 3 decimal places
filtered_df['OBP'] = (filtered_df['H'] +
                      filtered_df['BB'] +
                      filtered_df['HBP']) / (filtered_df['AB'] + 
                                             filtered_df['BB'] +
                                             filtered_df['HBP'] +
                                             filtered_df['SF'])
filtered_df['OBP'] = filtered_df['OBP'].round(3)

# calculate SLG and round to 3 decimal places
filtered_df['SLG'] = ((filtered_df['H'] - (filtered_df['2B'] + filtered_df['3B'] + filtered_df['HR'])) + # singles
                      (filtered_df['2B'] * 2) + # doubles
                      (filtered_df['3B'] * 3) + # triples
                      (filtered_df['HR'] * 4)) / filtered_df['AB'] # homeruns
filtered_df['SLG'] = filtered_df['SLG'].round(3)

# add OBP and SLG to create OPS
filtered_df['OPS'] = filtered_df['OBP'] + filtered_df['SLG']
filtered_df['OPS'] = filtered_df['OPS'].round(3)

# merge dataframes so our batting dataframe includes player names rather than only player IDs
filtered_df = pd.merge(filtered_df, names, on='playerID', how='left')

# export df with batting average, OBP, SLG, and OPS to csv
filtered_df.to_csv('2012_Batters.csv', index=False)