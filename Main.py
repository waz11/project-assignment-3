import sqlite3
import pandas as pd

data_path = "./files/database.sqlite"

def read_data(query):
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect(data_path)
    return pd.read_sql_query(query, con)

def main():
    ds_contries = read_data("SELECT * FROM Country")
    print(ds_contries)

if __name__ == "__main__":
    main()

