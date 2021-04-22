import ReadData

def main():
    match, player, player_attributes, team, team_attributes, country = ReadData.getTables()
    # print("match" + str(match.columns.values))
    # print("player" + str(player.columns.values))
    # print("player_attributes" + str(player_attributes.columns.values))
    # print("team" + str(team.columns.values))
    # print("team_attributes" + str(team_attributes.columns.values))
    # print("country" + str(country.columns.values))


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