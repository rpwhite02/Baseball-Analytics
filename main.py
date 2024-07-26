import streamlit as st
import pandas as pd
from scripts.batting_viz import hr_scatter
from scripts.pitching_viz import team_stat_starters

### EDIT TEXT USING MARKDOWN, STREAMLIT FORMATS LOOK LIKE SHIT

### KEEP RESEARCHING BETTER METHODS THIS FILE LOOKS LIKE SHIT

def home():
    st.title("Analyzing Baseball Trends and Insights")
    st.write("""
    ## Introduction
    This project provides an in-depth analysis of baseball statistics, including interactive visualizations and machine learning predictions
    to derive meaningful insights.
    
    ### Pages
    - **Batting Visualization**: Explore interactive charts that visualize offensive stats, focusing on individual players. Created using Plotly.
    - **Pitching Visualization**: View key pitching statistics such as ERA and strikeout rate, highlighting team performance. Also created with Plotly.
    """)


def batting():
    st.header("Top 10 Homerun Hitters in 2012 and Their Offensive Stats")

    batters = pd.read_csv('data/cleaned_csvs/2012_Batters.csv')
    top10_hr = batters.nlargest(10, 'HR')
    hr_scatter(top10_hr)

def pitching():
    st.header("Team Pitching Stats")

    starters = pd.read_csv('data/cleaned_csvs/2012_Starters.csv')
    team_stat_starters(starters)

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", ["Home", "Batting Visualizations", "Pitching Visualizations"])

    if selection == "Home":
        home()
    elif selection == "Batting Visualizations":
        batting()
    elif selection == "Pitching Visualizations":
        pitching()

if __name__ == "__main__":
    main()
