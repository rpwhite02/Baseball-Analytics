import pandas as pd
import plotly.express as px
import streamlit as st



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



def hr_scatter(dataframe):

    # Creating the scatter plot with Plotly
    fig = px.scatter(
        dataframe,
        x='G',
        y='HR',
        color='lgID',
        hover_name='playerID',
        hover_data={
            'G': True,
            'HR': True,
            'BattingAvg': True,
            'OBP': True,
            'OPS': True,
            'playerID': False
        },
        labels={
            'G': 'Games Played',
            'HR': 'Home Runs'
        },
        title='Games Played vs Top 10 HR Hitters in 2012'
    )

    # Update the layout for better appearance
    fig.update_layout(
        xaxis_title='Games Played',
        yaxis_title='Home Runs',
        title={
            'text': 'Games Played vs Home Runs for Top 10 HR Hitters in 2012',
            'x': 0.5
        }
    )

    fig.update_traces(marker=dict(size=15))  # Set all points to a constant size of 10

    st.plotly_chart(fig)
