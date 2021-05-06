from  sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split, GridSearchCV,cross_val_score

import  numpy as np
import Data as ReadData
from sklearn import metrics
def modelLogicReg(train_test_list):

    # split dataset into train and test data
    x_train, x_test, y_train, y_test = train_test_list

    # print((y_test))
    gnb = LogisticRegression(max_iter=1000)
    clf = gnb.fit(x_train,y_train)
    cls = clf.predict(x_test)
    print("Accuracy:", metrics.accuracy_score(y_test, cls))
    print("f1 score:", f1_score(y_test, cls,average="macro"))

    # train model with cv of 5
    cv_scores = cross_val_score(clf, x_test, y_test, cv=5)
    # print each cv score (accuracy) and average them
    print("cv_scores:")
    print(cv_scores)
    print('cv_scores mean:{}'.format(np.mean(cv_scores)))
    # return cls