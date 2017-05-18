from sklearn import datasets
from sklearn import svm
iris = datasets.load_iris()
print iris.data
print iris.target
clf = svm.SVC(gamma=0.001, C=100.)
print clf
clf.fit(iris.data[:-10], iris.target[:-10])
result=clf.predict(iris.data[-10:])
print ("predict")
print result
print ("actus")
print (iris.data[-10:])
print (iris.target[-10:])