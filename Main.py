import Data
import pandas as pd

def main():
    # read data
    match, player, player_attributes, team, team_attributes, league, country = Data.get_data()
    # queries
    match.query('season != "2015/2016"', inplace=True)

    # build a data frame:
    temp = pd.merge(match,country,left_on='country_id',right_on='id', how='left')
    # print(temp)

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