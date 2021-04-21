import pandas as pd
import sqlite3
DB_PATH = './datasets/us-baby-name/database.sqlite'
conn = sqlite3.connect('database.sqlite') # connecting to the database
c = conn.cursor() # creating a cursor object
x = c.execute("select * from Player")
for line in x.fetchall():
    print(line)
# c.execute("CREATE TABLE IF NOT EXISTS Names(State TEXT, Gender text , Name TEXT, Count INT , Year INT) " )
# c.execute("INSERT INTO Names(State,Gender,Name,Count, Year) SELECT State,Gender,Name,Count, Year FROM StateNames")
# c.close() # close the cursor


