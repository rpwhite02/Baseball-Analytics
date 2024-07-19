import streamlit as st
import pandas as pd
from scripts.pitching_viz import team_stat_starters

def app():
    st.header("Top 10 Homerun Hitters in 2012 and Their Offensive Stats")

    starters = pd.read_csv('data/cleaned_csvs/2012_Starters.csv')
    team_stat_starters(starters)