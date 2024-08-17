### WHERE TO PUT ML ALGORITHMS TO PREDICT OUTCOME BASED ON PITCHER, PITCH TYPE, AND SPEED
### NEURAL NETWORKS TO PREDICT PITCH SEQUENCING

import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score

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

    # print nroaml train-test results
    print('NON CV')
    print(confusion_matrix(y_test, y_pred))
    print(f'Accuracy: {accuracy:.3f}')

    # Print cross-validation results
    print('WITH CV')
    print(f'Cross-Validation Accuracy Scores: {cv_scores}')
    print(f'Mean Cross-Validation Accuracy: {cv_scores.mean():.3f}')
    print(f'Cross-Validation Standard Deviation: {cv_scores.std():.3f}')
