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
    st.title("Visualizing Baseball Trends and Insights")
    st.write("Welcome to the Home page! Use the sidebar to navigate to different visualizations.")

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