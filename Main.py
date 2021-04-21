import sqlite3
import pandas as pd
import numpy as np

import ReadData

def main():
    country = ReadData.get_table("SELECT * FROM Country")
    match = ReadData.get_table("SELECT * FROM Match")
    player = ReadData.get_table("SELECT * FROM Player")
    player_attributes = ReadData.get_table("SELECT * FROM Player_Attributes")
    team = ReadData.get_table("SELECT * FROM Team")
    team_attributes = ReadData.get_table("SELECT * FROM Team_Attributes")



if __name__ == "__main__":
    main()

