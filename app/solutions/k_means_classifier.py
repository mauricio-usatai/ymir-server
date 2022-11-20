from sklearn import datasets, neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from .solution import Solution

class KMeansClassifier(Solution):
    def apply(self, dataset_name):
        accuracy_threshold = 0.9

        if dataset_name == 'iris':
            dataset = datasets.load_iris()

        x_train, x_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.2)
        classifier = neighbors.KNeighborsClassifier()
        classifier.fit(x_train, y_train)
        predictions = classifier.predict(x_test)
        accuracy = accuracy_score(y_test, predictions)

        return True if accuracy >= accuracy_threshold else False