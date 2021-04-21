import sqlite3


# data_path = "./files/database.sqlite"

def main():
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect("./files/database.sqlite")

    cur = con.cursor()

    # The result of a "cursor.execute" can be iterated over by row
    for row in cur.execute('SELECT * from Country'):
        print(row)

    # Be sure to close the connection
    con.close()

if __name__ == "__main__":
    main()

