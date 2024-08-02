import pandas as pd
import plotly.express as px
import streamlit as st



def scatter_matrix(dataframe):
    
    fig = px.scatter_matrix(dataframe,
    dimensions=["BattingAvg", "OBP", "SLG", "OPS"],
    title="Scatter Matrix of Different Offensive Stats of Individual Players in 2012",
    hover_data={'PlayerName': True},
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
        hover_name='PlayerName',
        hover_data={
            'G': True,
            'HR': True,
            'BattingAvg': True,
            'OBP': True,
            'OPS': True,
            'PlayerName': False
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
