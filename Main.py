import Data

def main():
    data = Data.get_data_frames()
    print(data.keys())
    for df in data.values():
        Data.fillMissingValues(df)

if __name__ == "__main__":
    main()


# lev's query
#     dataTable = ReadData.get_table("SELECT Country.name AS Country, League.name AS League_Name, HomeTeam.team_long_name AS Home_Team ,AwayTeam.team_long_name AS Away_Team, Match.season, Match.stage, Match.home_team_goal, Match.away_team_goal \
#     FROM Match \
#     JOIN League,Country \
#     ON Country.id = Match.country_id and League.id = Match.league_id \
#     LEFT JOIN Team AS HomeTeam ON HomeTeam.team_api_id = Match.home_team_api_id \
#     LEFT JOIN Team as AwayTeam ON AwayTeam.team_api_id = Match.away_team_api_id \
#     WHERE Match.season <> '2015/2016'")
#     print(dataTable)