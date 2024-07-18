import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv('cleaned_csvs/2012_Batters.csv')

top5_hr = data.nlargest(5, 'HR')

top10_hr = data.nlargest(10, 'HR')

starters = pd.read_csv('cleaned_csvs/2012_Starters.csv')

def hr_scatter(dataframe):
    #st.title('Baseball Statistics: Comparing the Top 10 Home Run Hitters Offensive Stats')

    x = dataframe['G']
    y = dataframe['HR']
    labels = dataframe['playerID']

    fig, ax = plt.subplots()
    ax.scatter(x, y)

    for i in range(len(dataframe)):
        print(i)

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

team_stat_starters(starters)