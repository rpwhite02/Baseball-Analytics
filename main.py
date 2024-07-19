import streamlit as st
import pandas as pd
from scripts import batting_viz, pitching_viz
from scripts.batting_viz import hr_scatter
from scripts.pitching_viz import team_stat_starters

st.set_option('deprecation.showPyplotGlobalUse', False)

# Load data
batters = pd.read_csv('cleaned_csvs/2012_Batters.csv')
top10_hr = batters.nlargest(10, 'HR')

starters = pd.read_csv('cleaned_csvs/2012_Starters.csv')

# Define each page as a function
def home_page():
    st.title("Analyzing Baseball Trends and Insights")
    st.header("Welcome to the Home page! Use the sidebar to navigate to different parts of the analysis.")
    st.subheader("Batting Visualization contains interactive charts that visualize offensive stats, focusing on both indidivual players"
             " and entire teams. They're built using Plotly.")
    st.image("images/top10_hr.png", caption="Batting Visualization Example", use_column_width=True)
    st.subheader("Pitching Visualization contains interactive charts that visualize pitching stats for starting pitchers, relief pitchers,"
             " and entire team stats. The visualizations are also built using Plotly.")
    st.image("images/team_era.png", caption="Pitching Visualization Example", use_column_width=True)

def batting_page():
    st.header("Top 10 Homerun Hitters in 2012 and Their Offensive Stats")
    hr_scatter(top10_hr)

def pitching_page():
    st.header("ERA and Other Pitching Stats in 2012 by Team")
    team_stat_starters(starters)

# Dictionary to map page names to functions
PAGES = {
    "Home": home_page,
    "Batting Visualization": batting_page,
    "Pitching Visualization": pitching_page
}

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Call the selected page function
page = PAGES[selection]
page()