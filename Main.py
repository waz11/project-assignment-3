import Data as ReadData
import pandas as pn
import numpy as np
import knnModel

# import logisticRegressionModel
# import  turicreate as tc
# from sklearn.feature_selection import SelectKBest
# from sklearn.feature_selection import chi2
# from sklearn import preprocessing

def main():

    # load tables
    match = ReadData.get_table("select * from Match")
    # " where season != '2015/2016'")
    player_attributes = ReadData.get_table("SELECT * FROM Player_Attributes")
    team = ReadData.get_table("SELECT * FROM Team")
    df_league = ReadData.get_table("SELECT * FROM League")
    # team_attributes = ReadData.get_table("SELECT * FROM Team_Attributes")

    # calculated score performance of players - mean for each player
    selected_player_attributes = ['overall_rating']
    mean_rating = player_attributes.groupby('player_api_id')[selected_player_attributes].mean()

    # select the attributes we need to explore
    home_players = ['home_player_' + str(x + 1) for x in range(11)]
    away_players = ['away_player_' + str(x + 1) for x in range(11)]
    score_home_players = ['overall_rating' + str(x + 1) + '_home' for x in range(11)]
    score_away_players = ['overall_rating' + str(x + 1) + '_away' for x in range(11)]
    other_features = ['id', 'country_id', 'league_id', 'season', 'home_team_api_id', 'away_team_api_id', 'match_api_id','home_team_goal', 'away_team_goal']
    bet_features = ['B365H', 'B365D', 'B365A']
    teams_names = ['home_team', 'away_team']
    game_result = ['home_team_goal', 'away_team_goal', 'result']
    selected_season_league_attributes = ['league_name', 'season']
    selected_match_feature = home_players + away_players + other_features + bet_features

    # selected_team_attributes = ['home_team', 'away_team', 'home_team_goal','away_team_goal', 'result',
    # 'buildUpPlaySpeedHome', 'buildUpPlayPassingHome', 'defencePressureHome', 'buildUpPlaySpeedAway',
    # 'buildUpPlayPassingAway', 'defencePressureAway'] selected_relevant_feature = score_home_players +
    # score_away_players + selected_team_attributes + selected_season_league_attributes + bet_features
    df_match = match[selected_match_feature]

    # create new column : result  ->  home_team_win=1,  draw=0,  home_team_lose=-1
    conditions = [(df_match['home_team_goal'] - df_match['away_team_goal'] > 0),
                  (df_match['home_team_goal'] - df_match['away_team_goal'] == 0),
                  (df_match['home_team_goal'] - df_match['away_team_goal'] < 0)]
    result = [1, 0, -1]
    df_match = df_match.copy()
    df_match['result'] = np.select(conditions, result)

    # add for each match the performance score of the home and the away players
    for idx, player in enumerate(home_players):
        df_match = df_match.merge(mean_rating, left_on=player, right_on='player_api_id',
                                  suffixes=(None, str(idx + 1) + '_home'))
    df_match = df_match.rename(columns={'overall_rating': 'overall_rating1_home'}, inplace=False)

    for idx, player in enumerate(away_players):
        df_match = df_match.merge(mean_rating, left_on=player, right_on='player_api_id',
                                  suffixes=(None, str(idx + 1) + '_away'))
    df_match = df_match.rename(columns={'overall_rating': 'overall_rating1_away'}, inplace=False)

    # add the teams long names to the dataframe
    df_team_info = team[['team_api_id', 'team_long_name']]
    df_match = df_match.merge(df_team_info, left_on='home_team_api_id', right_on='team_api_id')
    df_match = df_match.rename(columns={'team_long_name': 'home_team'}, inplace=False)

    df_match = df_match.merge(df_team_info, left_on='away_team_api_id', right_on='team_api_id')
    df_match = df_match.rename(columns={'team_long_name': 'away_team'}, inplace=False)

    # add the league name to the dataframe
    df_league_info = df_league[['id', 'name']]
    df_match = df_match.merge(df_league_info, left_on='league_id', right_on='id')
    df_match = df_match.rename(columns={'name': 'league_name'}, inplace=False)

    # add team attribues
    #     df_team_info = team_attributes[['team_api_id','buildUpPlaySpeed','buildUpPlayPassing','defencePressure']]
    #
    # df_match = df_match.merge(df_team_info,left_on='home_team_api_id', right_on='team_api_id') df_match =
    # df_match.rename(columns={'buildUpPlaySpeed':'buildUpPlaySpeedHome','buildUpPlayPassing':'buildUpPlayPassingHome',
    # 'defencePressure':'defencePressureHome'}, inplace=False)
    #
    # df_match = df_match.merge(df_team_info,left_on='away_team_api_id', right_on='team_api_id') df_match =
    # df_match.rename(columns={'buildUpPlaySpeed':'buildUpPlaySpeedAway','buildUpPlayPassing':'buildUpPlayPassingAway',
    # 'defencePressure':'defencePressureAway'}, inplace=False)

    selected_relevant_feature2 = score_home_players + score_away_players + selected_season_league_attributes + bet_features + teams_names + game_result
    features_to_normilize = set(selected_relevant_feature2) - set(selected_season_league_attributes) - set(game_result) - set(teams_names)
    df_match = df_match[selected_relevant_feature2].drop_duplicates()
    df_to_normilize = df_match[list(features_to_normilize)]
    df_after_normilize = pn.DataFrame()
    for col in df_to_normilize.columns:
        df_after_normilize[col] = (df_to_normilize[col] - df_to_normilize[col].min()) / (df_to_normilize[col].max() - df_to_normilize[col].min())

    non_norm = selected_season_league_attributes+game_result+teams_names
    df_non_norm = df_match[non_norm]
    full_df = pn.concat([df_after_normilize, df_non_norm], axis=1)
    # print(full_df)
    full_df.to_csv("./files/df_full.csv")
    knn_model = knnModel.knn_model(full_df)
    print(knn_model)
    # evaluate = logisticRegressionModel.modelLogicReg(full_df)
    # print(evaluate)


    # player_attributes = ReadData.get_table("SELECT * FROM Player_Attributes")
    # player = ReadData.get_table("SELECT * FROM Player")
    # df = pn.concat([player, player_attributes], 1)
    # query = ReadData.get_table("SELECT * FROM Player, Player_Attributes WHERE Player.player_api_id == Player_Attributes.player_api_id")
    # dfPlayers = pn.DataFrame(query)
    #
    # dfPlayers.to_csv("./files/dfPlayers.csv")



if __name__ == "__main__":
    main()