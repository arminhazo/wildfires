import numpy as np
import pandas as pd

PATH = '../raw_data/wildfires.csv'

def counts_per_state(df):
    '''
    Calculates total amount of wildfires for each US state between 1992 and 2015
    '''
    number_of_fires = df.groupby('STATE').count()
    number_of_fires = number_of_fires['OBJECTID']

    return number_of_fires

def load_df(path=PATH):
    '''
    Loads csv file and converts it to pandas dataframe
    '''
    df = pd.read_csv(path, low_memory=False)

    return df

def get_counts():
    df = load_df()
    number_of_fires = counts_per_state(df)

    return number_of_fires


if __name__ == "__main__":
    print(get_counts())
