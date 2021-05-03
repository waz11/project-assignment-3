import sklearn.svm as svm
from sklearn.model_selection import train_test_split

def modelSVM(train_test_list):

    # split dataset into train and test data
    x_train, x_test, y_train, y_test = train_test_list

    #Create SVM Classifier:
    clf = svm.SVC(C=10,kernel='linear')

    # Fit the classifier to the data
    clf.fit(x_train, y_train)

    # check accuracy of our model on the test data
    accuracy = clf.score(x_test, y_test)

    print('Accuracy: %s' %(accuracy))
    # check accuracy of our model on the test data
    # accuracy = clf.
