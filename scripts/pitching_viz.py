import pandas as pd
import plotly.express as px
import streamlit as st

# group pitchers by team and analyze specific team stats like ERA, WHIP, K/9, etc.

# also separate starting pitchers and closing pitchers

relievers = pd.read_csv('data/cleaned_csvs/2012_Relievers.csv')

starters = pd.read_csv('data/cleaned_csvs/2012_Starters.csv')


def team_stat_starters(dataframe):

    st.header('')

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
        title='Teams Starting Pitching ERA',
        bargap=0.4
    )

    st.plotly_chart(fig)

    st.write('Data Table:')
    st.write(team_means)

#team_stat_starters(starters)