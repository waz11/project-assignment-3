from  sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier,GradientBoostingClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split, GridSearchCV

import  numpy as np
import ReadData
from sklearn import metrics
def modelLogicReg(df):
    features_x = set(df.columns) - set(['result'])

    X = df[list(features_x)]
    Y = df['result']
    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2, random_state=100)
    # print((y_test))
    gnb = LogisticRegression(max_iter=1000)
    clf = gnb.fit(x_train,y_train)
    cls = clf.predict(x_test)
    print("Accuracy:", metrics.accuracy_score(y_test, cls))
    print("f1 score:", f1_score(y_test, cls,average=None))
    return cls