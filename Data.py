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

def __read_tables():
    df = {}
    con = sqlite3.connect(data_path)
    for table_name in tables:
        query = "select * from " + table_name
        table = pd.read_sql_query(query, con)
        df[table_name] = pd.DataFrame(table)
    con.close()
    return df

def get_data():
    df = __read_tables()
    match = df['match']
    player = df['player']
    player_attributes = df['player_attributes']
    team = df['team']
    team_attributes = df['team_attributes']
    country = df['country']
    return match, player,player_attributes, team, team_attributes, country




