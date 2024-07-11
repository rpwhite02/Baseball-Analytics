import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('cleaned_csvs/2012_Batters.csv')

top5_hr = data.nlargest(5, 'HR')

top10_hr = data.nlargest(10, 'HR')

def hr_scatter(dataframe):
    #st.title('Baseball Statistics: Comparing the Top 10 Home Run Hitters Offensive Stats')

    x = dataframe['G']
    y = dataframe['HR']
    labels = dataframe['playerID']

    fig, ax = plt.subplots()
    ax.scatter(x, y)

    for i in range(len(dataframe)):
        print(i)

hr_scatter(top10_hr)