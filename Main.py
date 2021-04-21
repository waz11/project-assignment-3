import sqlite3
import pandas as pd

data_path = "./files/database.sqlite"

def read_data():
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect(data_path)
    return pd.read_sql_query("SELECT * FROM Country", con)

def main():
    ds = read_data()
    # print(ds)

if __name__ == "__main__":
    main()

