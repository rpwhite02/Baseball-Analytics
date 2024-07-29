import pandas as pd
import plotly.express as px
import streamlit as st

batting = pd.read_csv('data/cleaned_csvs/2012_Batters.csv')

fielding = pd.read_csv('data/cleaned_csvs/2012_Fielders.csv')

def scatter_matrix(batting_df, fielding_df):
    
    # filter the fielding dataframe to only include fielding percentage, all we really care about
    fielding_selected = fielding_df[['playerID', 'FieldingPct', 'E']]

    dataframe = pd.merge(batting_df, fielding_selected, on='playerID')

    fig = px.scatter_matrix(dataframe,
    dimensions=["BattingAvg", "OBP", "SLG", "OPS"],
    title="Scatter Matrix of Batting Average and Fielding Percentage of Players in 2012",
    labels={}) 
    
    fig.update_traces(diagonal_visible=False)

    st.plotly_chart(fig)


scatter_matrix(batting, fielding)