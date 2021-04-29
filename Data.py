import sqlite3
import pandas as pd
import numpy as np

data_path = "./files/database.sqlite"
home_players = ['home_player_' + str(x + 1) for x in range(11)]
away_players = ['away_player_' + str(x + 1) for x in range(11)]
problematic_attributes = home_players + away_players
def fillMissingValues(df):
    # for col in df.columns:
    #     if np.issubdtype(df[col].dtype, np.number) and col in problematic_attributes:
    #         df[col].fillna(0, inplace=True)
    #     if np.issubdtype(df[col].dtype, np.number):
    #         df[col].fillna(df[col].mean(), inplace=True)
    return df


def get_table(query):
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect(data_path)
    data = pd.read_sql_query(query, con)
    con.close()
    return fillMissingValues(data)







