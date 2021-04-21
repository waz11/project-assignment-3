import sqlite3
import pandas as pd
import numpy as np

data_path = "./files/database.sqlite"

def fillMissingValues(df):
    for col in df.columns:
        if np.issubdtype(df[col].dtype, np.number):
            df[col].fillna(df[col].mean(), inplace=True)
    return df;

def read_data(query):
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect(data_path)
    data = pd.read_sql_query(query, con)
    return fillMissingValues(data)

def main():
    country = read_data("SELECT * FROM Country")
    match = read_data("SELECT * FROM Match")
    player = read_data("SELECT * FROM Player")
    player_attributes = read_data("SELECT * FROM Player_Attributes")
    team = read_data("SELECT * FROM Team")
    team_atributes = read_data("SELECT * FROM Team_Attributes")




if __name__ == "__main__":
    main()

