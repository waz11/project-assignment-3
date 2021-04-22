import ReadData

def main():
    # country = ReadData.get_table("SELECT * FROM Country")
    # match = ReadData.get_table("select * from Match where season != '2015/2016'")
    # player = ReadData.get_table("SELECT * FROM Player")
    # player_attributes = ReadData.get_table("SELECT * FROM Player_Attributes")
    # team = ReadData.get_table("SELECT * FROM Team")
    # team_attributes = ReadData.get_table("SELECT * FROM Team_Attributes")
    dataTable = ReadData.get_table("SELECT Country.name AS Country, League.name AS League_Name, HomeTeam.team_long_name AS Home_Team ,AwayTeam.team_long_name AS Away_Team, Match.season, Match.stage, Match.home_team_goal, Match.away_team_goal \
FROM Match \
JOIN League,Country \
ON Country.id = Match.country_id and League.id = Match.league_id \
LEFT JOIN Team AS HomeTeam ON HomeTeam.team_api_id = Match.home_team_api_id \
LEFT JOIN Team as AwayTeam ON AwayTeam.team_api_id = Match.away_team_api_id \
WHERE Match.season <> '2015/2016'")
    print(dataTable)


if __name__ == "__main__":
    main()

