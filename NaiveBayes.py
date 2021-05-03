import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB


def naive_bayes(train_test_list):


    # split dataset into train and test data
    x_train, x_test, y_train, y_test = train_test_list

    # Create gnb classifier
    gnb = GaussianNB()

    # Fit the classifier to the data
    gnb.fit(x_train, y_train)

    # total = x_test.shape[0]
    # correct = (y_test == y_pred).sum()

    accuracy = gnb.score(x_test, y_test)

    print('Accuracy: %s' % (accuracy))

    # train model with cv of 5
    cv_scores = cross_val_score(gnb, x_test, y_test, cv=5)
    # print each cv score (accuracy) and average them
    print("cv_scores:")
    print(cv_scores)
    print('cv_scores mean:{}'.format(np.mean(cv_scores)))