
from sklearn.neighbors import *


def knn_model(df):
    training_features = set(df.columns) - set(['result'])
    train_data = df[list(training_features)]
    test_data = df['result']
    knn = KNeighborsClassifier(n_neighbors=5, weights='uniform')
    knn.fit(train_data, test_data)
    predict = knn.predict(test_data)
    print("Accuracy: ",knn.score(test_data, predict, sample_weight=None))
    # print(kneighbors_graph(X=None, n_neighbors=None, mode='connectivity'))
    return predict