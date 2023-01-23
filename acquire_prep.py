#Import needed items
import numpy as np
import pandas as pd
import env
import os

# acquire the data.  Data is in the repo as a .csv document
#read in the csv

def get_diabetes_data():
    '''
    This function checks if the diabetes data is saved locally. 
    '''
    filename = 'diabetes.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename).iloc[:,1:]


