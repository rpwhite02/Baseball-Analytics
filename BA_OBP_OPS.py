import pandas as pd

batting_df = pd.read_csv('csvs/Batting.csv')

filtered_2012 = batting_df[batting_df['yearID'] == 2012]

print(filtered_2012)