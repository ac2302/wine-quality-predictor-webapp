import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import pickle

# importing the dataset
dataset_white = pd.read_csv('datasets/white.csv')
dataset_red = pd.read_csv('datasets/red.csv')
X_white = dataset_white.iloc[:, :-1]
y_white = dataset_white.iloc[:, -1]
X_red = dataset_red.iloc[:, :-1]
y_red = dataset_red.iloc[:, -1]

# training the models
white_model = DecisionTreeRegressor()
white_model.fit(X_white, y_white)
red_model = DecisionTreeRegressor()
red_model.fit(X_red, y_red)

def msg(m):
    print(m)
    return(m)

# pickling them
with open('model', 'wb') as f:
    pickle.dump({'red': red_model,
                 'white': white_model}, f)