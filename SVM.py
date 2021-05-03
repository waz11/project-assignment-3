import sklearn.svm as svm
from sklearn.model_selection import train_test_split

def modelSVM(df):

    features_x = set(df.columns) - set(['result'])

    X = df[list(features_x)]
    Y = df['result']
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=100)

    #Create SVM Classifier:
    clf = svm.SVC(C=10,kernel='linear')

    # Fit the classifier to the data
    clf.fit(x_train, y_train)

    # check accuracy of our model on the test data
    accuracy = clf.score(x_test, y_test)

    print('Accuracy: %s' %(accuracy))
    # check accuracy of our model on the test data
    # accuracy = clf.
