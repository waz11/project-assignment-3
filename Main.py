import ReadData

def main():
    country = ReadData.get_table("SELECT * FROM Country")
    match = ReadData.get_table("select * from Match where season != '2015/2016'")
    player = ReadData.get_table("SELECT * FROM Player")
    player_attributes = ReadData.get_table("SELECT * FROM Player_Attributes")
    team = ReadData.get_table("SELECT * FROM Team")
    team_attributes = ReadData.get_table("SELECT * FROM Team_Attributes")

if __name__ == "__main__":
    main()

