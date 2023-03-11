from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# load the iris dataset
iris = load_iris()

# split the data into features (X) and labels (y)
X = iris.data
y = iris.target

# split the data into training and testing sets
trainX, testX, trainY, testY = train_test_split(X, y, test_size=0.6, random_state=3)

# create a Naive Bayes classifier object
gnb = GaussianNB()

# train the model using the training data
gnb.fit(trainX, trainY)

# use the trained model to make predictions on the test data
predictY = gnb.predict(testX)

# print the accuracy of the model
print("The model's accuracy is shown below:")
print(metrics.accuracy_score(testY, predictY)*100)
