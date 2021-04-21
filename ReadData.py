import sqlite3
import pandas as pd
import numpy as np

data_path = "./files/database.sqlite"

def fillMissingValues(df):
    for col in df.columns:
        if np.issubdtype(df[col].dtype, np.number):
            df[col].fillna(df[col].mean(), inplace=True)
    return df;

def get_table(query):
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect(data_path)
    data = pd.read_sql_query(query, con)
    return fillMissingValues(data)


