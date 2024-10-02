### WHERE TO PUT ML ALGORITHMS TO PREDICT OUTCOME BASED ON PITCHER, PITCH TYPE, AND SPEED
### NEURAL NETWORKS TO PREDICT PITCH SEQUENCING

import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, classification_report
from sklearn.pipeline import Pipeline
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

    # Create pipeline with model and its parameters and include scaler
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', LogisticRegression(
            multi_class='multinomial', solver='lbfgs', max_iter=1000)
        )
    ])

    # Fit pipeline on training data
    pipeline.fit(X_train, y_train)

    # Predict outcomes on the Test X
    y_pred = pipeline.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy on the Test Set: {accuracy:.3f}')

    # Classification report with precision and recall
    print('Classification Report on Test Set:')
    print(classification_report(y_test, y_pred))

    # Create confusion matrix display
    fig, ax = plt.subplots()
    ConfusionMatrixDisplay.from_estimator(pipeline, X_test, y_test, cmap="Blues", ax=ax)

    # Perform cross-validation with the pipeline
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = cross_val_score(pipeline, X, y, cv=skf, scoring='accuracy')

    # print nroaml train-test results
    plt.show()
    # st.write('NON CV')
    # st.write('Confusion Matrix Display:')
    # st.pyplot(fig)
    # st.write(f'Accuracy: {accuracy:.3f}')

    # Print cross-validation results
    print('Cross-Validation Accuracy Scores:', cv_scores)
    print(f'Mean Cross-Validation Accuracy: {cv_scores.mean():.3f}')
    print(f'Cross-Validation Standard Deviation: {cv_scores.std():.3f}')
    # st.write('WITH CV')
    # st.write('Cross-Validation Accuracy Scores:')
    # st.write(cv_scores)
    # st.write(f'Mean Cross-Validation Accuracy: {cv_scores.mean():.3f}')
    # st.write(f'Cross-Validation Standard Deviation: {cv_scores.std():.3f}')

jv_ff = pd.read_csv('data/pitcher_csvs/verlander_pitches/verlander_FF.csv') 
# jv_sl = pd.read_csv('data/pitcher_csvs/verlander_pitches/verlander_SL.csv') 
# jv_cu = pd.read_csv('data/pitcher_csvs/verlander_pitches/verlander_CU.csv') 
# jv_fc = pd.read_csv('data/pitcher_csvs/verlander_pitches/verlander_FC.csv') 
# jv_ft = pd.read_csv('data/pitcher_csvs/verlander_pitches/verlander_FT.csv') 
# jv_ch = pd.read_csv('data/pitcher_csvs/verlander_pitches/verlander_CH.csv')
jv_predictions(jv_ff)

# FF with 3 folds is 0.327 CV, 0.350 without CV. FF with 5 folds is 0.328 CV, 0.350 without CV
# SL with 3 folds is 0.324 CV, 0.319 without CV. SL with 5 folds is 0.328 CV, 0.319 withotu CV
# CU with 3 folds is 0.334 CV, 0.335 without CV. CU with 5 folds is 0.322 CV, 0.335 without CV
# FC with 3 folds is 0.265 CV, 0.429 without CV. FC with 5 folds is 0.210 CV, 0.429 without CV (SMALL SAMPLE)
# FT with 3 folds is 0.167 CV, 0.667 without CV. FT with 2 folds is 0.333 CV, 0.667 without CV (SMALL SAMPLE)
# CH with 3 folds is 0.255 CV, 0.284 without CV. CH with 5 folds is 0.270 CV, 0.284 without CV