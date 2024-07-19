import streamlit as st
import pandas as pd
from scripts.batting_viz import hr_scatter

def app():
    st.header("Top 10 Homerun Hitters in 2012 and Their Offensive Stats")

    batters = pd.read_csv('data/cleaned_csvs/2012_Batters.csv')
    top10_hr = batters.nlargest(10, 'HR')
    hr_scatter(top10_hr)
