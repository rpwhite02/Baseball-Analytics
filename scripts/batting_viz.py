import pandas as pd
import plotly.express as px
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

data = pd.read_csv('cleaned_csvs/2012_Batters.csv')

top5_hr = data.nlargest(5, 'HR')

top10_hr = data.nlargest(10, 'HR')

def hr_scatter(dataframe):
    st.header('Comparing the Top 10 Home Run Hitters Offensive Stats')

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

    st.write(fig)

    st.write('Data Table:')
    st.write(dataframe)

hr_scatter(top10_hr)