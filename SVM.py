from sklearn.metrics import f1_score
import numpy as np
import sklearn.svm as svm
from sklearn.model_selection import cross_val_score

def modelSVM(train_test_list):

    # split dataset into train and test data
    x_train, x_test, y_train, y_test = train_test_list

    #Create SVM Classifier:
    clf = svm.SVC(C=10,kernel='linear')

    # Fit the classifier to the data
    clf.fit(x_train, y_train)

    # check accuracy of our model on the test data
    accuracy = clf.score(x_test, y_test)
    predict = clf.predict(x_test)

    print('Accuracy: %s' %(accuracy))
    print("f1 score:", f1_score(y_test, predict, average="macro"))

    # train model with cv of 5
    cv_scores = cross_val_score(clf, x_test, y_test, cv=5)

    # print each cv score (accuracy) and average them
    print("cv_scores:")
    print(cv_scores)
    print('cv_scores mean:{}'.format(np.mean(cv_scores)))
