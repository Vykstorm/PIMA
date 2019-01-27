'''
This file contains helper methods used accross all scripts in order to load / preprocess data in the PIMA dataset
'''


# Import statements
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from keras.utils import to_categorical


def scale_features(data):
    # This method scales down all features so that they are in the interval [0, 1] or [-1, 1]
    # Pregnancies and age features are scaled using min-max scaling
    # The other: Glucose, BloodPressure, SkinThickness, Insulin, BMI and DiabetesPedigreeFunction are scaled
    # using standard normal distribution scaling
    mm_scaler = MinMaxScaler()
    std_scaler = StandardScaler()
    
    for feature in ('Pregnancies', 'Age'):
        data[feature] = mm_scaler.fit_transform(data[[feature]])
    
    for feature in ('Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction'):
        data[feature] = std_scaler.fit_transform(data[[feature]])


def clean_outliers(data):
    # This method clean dataset outliers
    # TODO
    pass


def preprocess(data):
    # This method preprocess the dataset: scales down features & clean outliers inplace
    scale_features(data)
    clean_outliers(data)
    
def get_features(data):
    # Returns a pandas dataframe object with only the features of the samples of the dataset (without the outcome column)
    return data.drop(columns=['Outcome'])
  
def get_outcome(data):
    # Returns a single pandas Series object with the outcome labels for each sample
    return data['Outcome']

def get_categorical_outcome(data):
    # Returns a numpy array with 2 columns and the same number of rows as samples in the dataset. The first column is 1 if
    # the given sample has the value 0 on the outcome variable. The second row will have the value 1. Otherwise if the sample
    # has the value 1 in the outcome, the row will be [0, 1]
    return to_categorical(get_outcome(data))
    
def load_dataset():
    # This method loads the PIMA dataset and preprocess it (if preprocess parameter is set to True).
    # Then its returned as a DataFrame object
    data = pd.read_csv('../data/diabetes.csv')
    return data

if __name__ == '__main__':
    # Unitary test of this module
    data = load_dataset()