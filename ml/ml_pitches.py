### WHERE TO PUT ML ALGORITHMS TO PREDICT OUTCOME BASED ON PITCHER, PITCH TYPE, AND SPEED
### NEURAL NETWORKS TO PREDICT PITCH SEQUENCING

import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
import matplotlib.pyplot as plt
import streamlit as st

def jv_predictions(dataframe):
# load in data
    #fastballs = pd.read_csv('data/pitcher_csvs/verlander_pitches/verlander_FF.csv')

    # change string lefty or righty to number values (0 and 1)
    dataframe = pd.get_dummies(dataframe, columns=['stand'])

    # print(fastballs.columns)

    # define features and target
    X = dataframe[['break_angle', 'break_length', 'nasty', 'pitch_num', 'spin_dir', 'spin_rate',
                'start_speed', 'x', 'y', 'stand_left', 'stand_right']]
    y = dataframe['code']

    # split the data into train and test, test size is 20%
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # standardize the features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # initialize and train model
    model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
    model_cv = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
    model.fit(X_train, y_train)

    # predict outcomes on test set using cross validation
    cv_scores = cross_val_score(model_cv, X, y, cv=5, scoring='accuracy')

    # predict outcomes on test set using normal train/test no cross validation
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Create confusion matrix display
    fig, ax = plt.subplots()
    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, cmap="Blues", ax=ax)

    # print nroaml train-test results
    st.write('NON CV')
    st.write('Confusion Matrix Display:')
    st.pyplot(fig)
    st.write(f'Accuracy: {accuracy:.3f}')

    # Print cross-validation results
    st.write('WITH CV')
    st.write('Cross-Validation Accuracy Scores:')
    st.write(cv_scores)
    st.write(f'Mean Cross-Validation Accuracy: {cv_scores.mean():.3f}')
    st.write(f'Cross-Validation Standard Deviation: {cv_scores.std():.3f}')

# jv_ff = pd.read_csv('data/pitcher_csvs/verlander_pitches/verlander_FF.csv') 
# jv_sl = pd.read_csv('data/pitcher_csvs/verlander_pitches/verlander_SL.csv') 
# jv_cu = pd.read_csv('data/pitcher_csvs/verlander_pitches/verlander_CU.csv') 
# jv_fc = pd.read_csv('data/pitcher_csvs/verlander_pitches/verlander_FC.csv') 
# jv_ft = pd.read_csv('data/pitcher_csvs/verlander_pitches/verlander_FT.csv') 
# jv_ch = pd.read_csv('data/pitcher_csvs/verlander_pitches/verlander_CH.csv')
# jv_predictions(jv_ch)

# FF with 3 folds is 0.327 CV, 0.350 without CV. FF with 5 folds is 0.328 CV, 0.350 without CV
# SL with 3 folds is 0.324 CV, 0.319 without CV. SL with 5 folds is 0.328 CV, 0.319 withotu CV
# CU with 3 folds is 0.334 CV, 0.335 without CV. CU with 5 folds is 0.322 CV, 0.335 without CV
# FC with 3 folds is 0.265 CV, 0.429 without CV. FC with 5 folds is 0.210 CV, 0.429 without CV (SMALL SAMPLE)
# FT with 3 folds is 0.167 CV, 0.667 without CV. FT with 2 folds is 0.333 CV, 0.667 without CV (SMALL SAMPLE)
# CH with 3 folds is 0.255 CV, 0.284 without CV. CH with 5 folds is 0.270 CV, 0.284 without CV