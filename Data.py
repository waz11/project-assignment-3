import sqlite3
import pandas as pd
import numpy as np

data_path = "./files/database.sqlite"
tables = ['match', 'player', 'player_attributes', 'team', 'team_attributes', 'country']

def fillMissingValues(df):
    for col in df.columns:
        if np.issubdtype(df[col].dtype, np.number):
            df[col].fillna(df[col].mean(), inplace=True)
    return df;

def __get_table(table_name):
    con = sqlite3.connect(data_path)
    query = "select * from " + table_name
    table = pd.read_sql_query(query, con)
    con.close()
    return table

def get_data_frames():
    df = {}
    for table_name in tables:
        table = __get_table(table_name)
        df[table_name] = pd.DataFrame(table)
    return df


