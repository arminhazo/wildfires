# Data preparation

import sqlite3 as sql
import pandas as pd
import numpy as np


SQL_PATH = '../raw_data/FPA_FOD_20170508.sqlite'
TABLE = 'fires'
ORDER_BY = 'FIRE_YEAR'
CSV_PATH = '../raw_data/wildfires.csv'


def sql_to_df(load_path, table, order_by):
    '''
    Transforms the fires table from the sqlite database into pandas dataframe
    '''
    conn = sql.connect(load_path)
    db = conn.cursor()
    query = f"""
    SELECT * FROM '{table}' ORDER BY ?
    """
    db.execute(query, (order_by,))

    rows = db.fetchall()
    wildfires_df = pd.DataFrame(rows)

    # assign column names
    wildfires_df.columns = [i[0] for i in db.description]

    return wildfires_df

def df_to_csv(df, save_path):
    '''
    Saves the python database to a csv file
    '''
    df.to_csv(save_path)


def run_preparation(SQL_PATH=SQL_PATH, TABLE=TABLE, ORDER_BY=ORDER_BY, CSV_PATH=CSV_PATH):
    df = sql_to_df(SQL_PATH, TABLE, ORDER_BY)
    df_to_csv(df, CSV_PATH)

if __name__ == "__main__":
    run_preparation()
