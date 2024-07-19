import streamlit as st
import pandas as pd
from scripts.batting_viz import hr_scatter
from scripts.pitching_viz import team_stat_starters

st.set_option('deprecation.showPyplotGlobalUse', False)

### EDIT TEXT USING MARKDOWN, STREAMLIT FORMATS LOOK LIKE SHIT

def home():
    st.title("Analyzing Baseball Trends and Insights")

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

### KEEP RESEARCHING BETTER METHODS THIS FILE LOOKS LIKE SHIT