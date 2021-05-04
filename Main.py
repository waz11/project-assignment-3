import operator
from sklearn.feature_selection import VarianceThreshold
import Data as ReadData
import pandas as pn
import numpy as np
import logisticRegressionModel as lr
import knnModel as kn
import SVM as svm
import NaiveBayes as nb
from sklearn.model_selection import train_test_split



def main():
    # load tables

    # Regular Table:
    # match = ReadData.get_table("select * from Match")
    # Big Table:
    match = ReadData.get_table("SELECT Match.*,AVG(HomeTeam.buildUpPlayDribbling) AS Home_Team_buildUpPlayDribbling,\
    AVG(HomeTeam.buildUpPlayPassing) AS Home_Team_buildUpPlayPassing, AVG(HomeTeam.buildUpPlaySpeed) AS Home_Team_buildUpPlaySpeed,\
    AVG(HomeTeam.chanceCreationCrossing) AS Home_Team_chanceCreationCrossing,AVG(HomeTeam.chanceCreationPassing) AS Home_Team_chanceCreationPassing,\
    AVG(HomeTeam.chanceCreationShooting) AS Home_Team_chanceCreationShooting,AVG(HomeTeam.defenceAggression) AS Home_Team_defenceAggression,\
    AVG(HomeTeam.defencePressure) AS Home_Team_defencePressure,AVG(HomeTeam.defenceTeamWidth) AS Home_Team_defenceTeamWidth,\
    AVG(AwayTeam.buildUpPlayDribbling) AS Away_Team_buildUpPlayDribbling, AVG(AwayTeam.buildUpPlayPassing) AS Away_Team_buildUpPlayPassing,\
    AVG(AwayTeam.buildUpPlaySpeed) AS Away_Team_buildUpPlaySpeed, AVG(AwayTeam.chanceCreationCrossing) AS Away_Team_chanceCreationCrossing,\
    AVG(AwayTeam.chanceCreationPassing) AS Away_Team_chanceCreationPassing,AVG(AwayTeam.chanceCreationShooting) AS Away_Team_chanceCreationShooting,\
    AVG(AwayTeam.defenceAggression) AS Away_Team_defenceAggression,AVG(AwayTeam.defencePressure) AS Away_Team_defencePressure,\
    AVG(AwayTeam.defenceTeamWidth) AS Away_Team_defenceTeamWidth\
    FROM Match LEFT JOIN Team_Attributes AS HomeTeam ON HomeTeam.team_api_id = Match.home_team_api_id\
    LEFT JOIN Team_Attributes as AwayTeam ON AwayTeam.team_api_id = Match.away_team_api_id\
	GROUP BY Match.id")
    player_attributes = ReadData.get_table("SELECT * FROM Player_Attributes")
    # team = ReadData.get_table("SELECT * FROM Team")
    # df_league = ReadData.get_table("SELECT * FROM League")
    # team_attributes = ReadData.get_table("SELECT * FROM Team_Attributes")

    # calculated score performance  of players
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
    # selected_season_league_attributes = ['league_name', 'season']

    # Delete Season Here:
    selected_season_league_attributes = ['season']

    #Team Attributes:
    selected_team_attributes = ['Home_Team_buildUpPlayDribbling', 'Home_Team_buildUpPlayPassing',
                                'Home_Team_buildUpPlaySpeed', \
                                'Home_Team_chanceCreationCrossing', 'Home_Team_chanceCreationPassing',
                                'Home_Team_chanceCreationShooting', \
                                'Home_Team_defenceAggression', 'Home_Team_defencePressure',
                                'Home_Team_defenceTeamWidth', 'Away_Team_buildUpPlayDribbling', \
                                'Away_Team_buildUpPlayPassing', 'Away_Team_buildUpPlaySpeed',
                                'Away_Team_chanceCreationCrossing', 'Away_Team_chanceCreationPassing', \
                                'Away_Team_chanceCreationShooting', 'Away_Team_defenceAggression',
                                'Away_Team_defencePressure', 'Away_Team_defenceTeamWidth']

    #Team Attributes:
    selected_match_feature = home_players + away_players + other_features + bet_features + selected_team_attributes

    # selected_match_feature = home_players + away_players + other_features + bet_features

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



    avg_team_preformance = ['avg_home_preformance','avg_away_preformance']
    #without season:
    # selected_relevant_feature2 = bet_features + avg_team_preformance + game_result

    # Old One:
    # selected_relevant_feature2 = bet_features + avg_team_preformance + game_result + selected_season_league_attributes

    #Team Attributes:
    selected_relevant_feature2 = bet_features + avg_team_preformance + selected_team_attributes + selected_season_league_attributes + game_result

    features_to_normilize = set(selected_relevant_feature2) - set(game_result)
    home_col = df_match[score_home_players]
    df_match['avg_home_preformance'] = df_match[score_home_players].mean(axis='columns')
    df_match['avg_away_preformance'] = df_match[score_away_players].mean(axis='columns')
    df_match['season'] = df_match['season'].apply(lambda x: int(x.split('/')[1][2:]))
    df_match = df_match.drop_duplicates()
    df_to_normilize = df_match[list(features_to_normilize)]
    df_after_normilize = pn.DataFrame()
    for col in df_to_normilize.columns:
        df_after_normilize[col] = (df_to_normilize[col] - df_to_normilize[col].min()) / (df_to_normilize[col].max() - df_to_normilize[col].min())

    # non_norm = 'result'
    non_norm = ['result']
    df_non_norm = df_match[non_norm]
    full_df = pn.concat([df_after_normilize, df_non_norm], axis=1)
    print("Data Size:")
    print("Before Dropping: ")
    print(full_df.shape)

    full_df_with_outlier = full_df
    full_df_with_outlier_without_team_attribute = full_df.drop(columns=selected_team_attributes,axis=1)

    #******************************Delete Outlier Data:*********************************************
    id_to_delete = []
    for col in full_df:
        colData = full_df[col]
        id_to_delete += full_df[(np.abs(colData - colData.mean()) > (2.5 * colData.std()))].index.values.tolist()
    full_df = full_df.drop(full_df.index[id_to_delete])

    full_df_without_outlier = full_df
    full_df_without_outlier_without_team_attribute = full_df.drop(selected_team_attributes,axis=1)

    print("After Dropping: ")
    print(full_df.shape)

    # full_df.to_csv("./files/df_full_with_season.csv",index=False)
    # full_df = pn.read_csv("./files/df_full.csv")

    # full_df.drop('result', axis=1).apply(lambda x: x.corr(full_df.result))
    #
    corr_dict = {}
    for col in full_df.columns:
        corr_dict[col] = np.corrcoef(full_df[col], full_df['result'])[1][0]
    sorted_d = sorted(corr_dict.items(), key=operator.itemgetter(1), reverse=True)
    choose_features = [key for key,val in corr_dict.items() if val>0.1]
    new_df = full_df[choose_features]
    # print(full_df)


    # X = full_df
    # sel = VarianceThreshold(threshold=(.1 * (1 - .1)))
    # print(sel.fit_transform(X))


    new_df.to_csv("./files/new_df.csv", index=False)

    train_test_list = train_test(new_df)
    print("Data with new data with team attributes: ")
    print("Logic Rec: \n")
    lr.modelLogicReg(train_test_list)
    print("\n KNN: \n")
    kn.knn_model(train_test_list)
    print("\n SVM - SVC: \n")
    svm.modelSVM(train_test_list)
    print("\n Naive-Bayes: \n")
    nb.naive_bayes(train_test_list)



    # ************************Models:***************************

    print('\n')

    #Models:
    '''
    train_test_list = train_test(full_df_with_outlier)
    print("Data with outlier data with team attributes: ")
    print("Logic Rec: \n")
    lr.modelLogicReg(train_test_list)
    print("\n KNN: \n")
    kn.knn_model(train_test_list)
    print("\n SVM - SVC: \n")
    svm.modelSVM(train_test_list)
    print("\n Naive-Bayes: \n")
    nb.naive_bayes(train_test_list)

    print('\n')


    print("Data with outlier data without team attributes: ")
    train_test_list = train_test(full_df_with_outlier_without_team_attribute)
    print("Logic Rec: \n")
    lr.modelLogicReg(train_test_list)
    print("\n KNN: \n")
    kn.knn_model(train_test_list)
    print("\n SVM - SVC: \n")
    svm.modelSVM(train_test_list)
    print("\n Naive-Bayes: \n")
    nb.naive_bayes(train_test_list)

    print('\n')

    print("Data without outlier data , with team attributes: ")
    train_test_list = train_test(full_df_without_outlier)
    print("Logic Rec: \n")
    lr.modelLogicReg(train_test_list)
    print("\n KNN: \n")
    kn.knn_model(train_test_list)
    print("\n SVM - SVC: \n")
    svm.modelSVM(train_test_list)
    print("\n Naive-Bayes: \n")
    nb.naive_bayes(train_test_list)

    print('\n')
    train_test_list = train_test(full_df_without_outlier_without_team_attribute)
    print("Data without outlier data , without team attributes: ")
    print("Logic Rec: \n")
    lr.modelLogicReg(train_test_list)
    print("\n KNN: \n")
    kn.knn_model(train_test_list)
    print("\n SVM - SVC: \n")
    svm.modelSVM(train_test_list)
    print("\n Naive-Bayes: \n")
    nb.naive_bayes(train_test_list)
    '''





def train_test(df):
    training_features = set(df.columns) - set(['result'])
    x = df[list(training_features)]
    y = df['result']

    # split dataset into train and test data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    return [x_train, x_test, y_train, y_test]


if __name__ == "__main__":
    main()