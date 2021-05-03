
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