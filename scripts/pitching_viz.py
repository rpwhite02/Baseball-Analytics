import pandas as pd
import plotly.express as px
import streamlit as st

# group pitchers by team and analyze specific team stats like ERA, WHIP, K/9, etc.

# also separate starting pitchers and closing pitchers

st.set_option('deprecation.showPyplotGlobalUse', False)

relievers = pd.read_csv('cleaned_csvs/2012_Relievers.csv')

starters = pd.read_csv('cleaned_csvs/2012_Starters.csv')

def team_era_starters(dataframe):
    st.header('Analyzing Team Pitching Stats')

    