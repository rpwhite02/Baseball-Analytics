import streamlit as st
import pandas as pd
from batting_viz import hr_scatter
from pitching_viz import team_era_starters

st.set_option('deprecation.showPyplotGlobalUse', False)

batters = pd.read_csv('cleaned_csvs/2012_Batters.csv')
top10_hr = batters.nlargest(10, 'HR')

starters = pd.read_csv('cleaned_csvs/2012_Starters.csv')


def main():
    st.title("Visualizing Baseball Trends and Insights")

    st.header("Module 1 Output")
    hr_scatter(top10_hr)

    st.header("Module 2 Output")
    team_era_starters()

if __name__ == "__main__":
    main()