import sqlite3
import pandas as pd
import numpy as np

data_path = "./files/database.sqlite"

def fillMissingValues(df):
    for col in df.columns:
        if np.issubdtype(df[col].dtype, np.number):
            df[col].fillna(df[col].mean(), inplace=True)
    return df;

def __get_table(query):
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect(data_path)
    df = pd.read_sql_query(query, con)
    con.close()
    return df

def getTables():
    match = __get_table("select * from Match where season != '2015/2016'")
    player = __get_table("SELECT * FROM Player")
    player_attributes = __get_table("SELECT * FROM Player_Attributes")
    team = __get_table("SELECT * FROM Team")
    team_attributes = __get_table("SELECT * FROM Team_Attributes")
    country = __get_table("SELECT * FROM Country")

    return match, player, player_attributes, team, team_attributes, country


