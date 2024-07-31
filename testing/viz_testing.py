import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

batting = pd.read_csv('cleaned_csvs/2012_Batters.csv')

top5_hr = batting.nlargest(5, 'HR')

top10_hr = batting.nlargest(10, 'HR')

starters = pd.read_csv('cleaned_csvs/2012_Starters.csv')

fielding = pd.read_csv('data/cleaned_csvs/2012_Fielders.csv')

def hr_scatter(dataframe):
    #st.title('Baseball Statistics: Comparing the Top 10 Home Run Hitters Offensive Stats')

    x = dataframe['G']
    y = dataframe['HR']
    labels = dataframe['PlayerName']

    fig, ax = plt.subplots()
    ax.scatter(x, y)

    for i in range(len(dataframe)):
        print(i)

# hr_scatter(batting)



def team_stat_starters(dataframe):

    # group data by teamID
    # calculate team ERA, WHIP, K/9, BB/9, HR/9, and K%
    
    statistics = ['ERA', 'WHIP', 'K/9', 'BB/9', 'HR/9', 'KPct']

    team_means = dataframe.groupby(['teamID', 'lgID'])[statistics].mean().round(3).reset_index()
    team_means = team_means.sort_values(by='ERA', ascending=False)

    fig = px.bar(team_means,
                       x="teamID",
                       y="ERA",
                       color="lgID",
                       hover_name="teamID",
                       hover_data={
                           'ERA': True,
                           'WHIP': True,
                           'K/9': True,
                           'BB/9': True,
                           'HR/9': True,
                           'KPct': True
                       },

                       labels={
                           'teamID': 'Team',
                           'sum of ERA': 'ERA',
                           'lgID': 'League'
                       }

    )

    fig.update_layout(
        xaxis_title='Teams',
        yaxis_title='ERA',
        bargap=0.4
    )

    fig.show()

# team_stat_starters(starters)



def scatter_matrix(batting_df, fielding_df):
    
    # filter the fielding dataframe to only include fielding percentage, all we really care about
    fielding_selected = fielding_df[['PlayerName', 'FieldingPct', 'E']]

    dataframe = pd.merge(batting_df, fielding_selected, on='playerID')

    fig = px.scatter_matrix(dataframe,
    dimensions=["BattingAvg", "OBP", "SLG", "OPS"],
    title="Scatter Matrix of Batting Average and Fielding Percentage of Players in 2012",
    labels={}) 
    
    fig.update_traces(diagonal_visible=False)

# scatter_matrix(batting, fielding)