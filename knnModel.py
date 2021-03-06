from sklearn.metrics import f1_score
import numpy as np
from sklearn.neighbors import *
from sklearn.model_selection import train_test_split, cross_val_score


def knn_model(train_test_list):
    # training_features = set(df.columns) - set(['result'])
    # x = df[list(training_features)]
    # y = df['result']
    #
    # # split dataset into train and test data
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)  # , stratify=y

    # split dataset into train and test data
    x_train, x_test, y_train, y_test = train_test_list

    # Create KNN classifier
    knn = KNeighborsClassifier(n_neighbors=55, weights='uniform')

    # Fit the classifier to the data
    knn.fit(x_train, y_train)

    # show predictions on the test data
    predict = knn.predict(x_test)

    # check accuracy of our model on the test data
    accuracy = knn.score(x_test, y_test)

    print("Accuracy KNN: ",accuracy)
    print("f1 score:", f1_score(y_test, predict, average="macro"))

    # train model with cv of 5
    cv_scores = cross_val_score(knn, x_test, y_test, cv=5)
    # print each cv score (accuracy) and average them
    print("cv_scores:")
    print(cv_scores)
    print('cv_scores mean:{}'.format(np.mean(cv_scores)))

