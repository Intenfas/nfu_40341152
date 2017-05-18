#coding=utf-8
from sklearn import datasets
from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)
digits = datasets.load_digits()
clf.fit(digits.data[:100], digits.target[:100])
result=clf.predict(digits.data[1])
a=[0,0,10,10,10,20,10,5,0,0,5,5,8,8,10,0,0,0,0,0,0,5,10,0,0,5,5,5,20,10,5,0,0,3,5,10,20,0,0,0,0,0,0,10,5,0,0,0,0,0,5,10,0,0,0,0,0,0,10,5,0,0,0,0]
result2=clf.predict(a)
print ("預測")
print (result2)
print ("實際")
print ("7")
import matplotlib.pyplot as plot
plot.figure(1, figsize=(3, 3))
#plot.imshow(digits.images[1], cmap=plot.cm.gray_r, interpolation='nearest')
#plot.show()
plot.imshow(digits.images[7], cmap=plot.cm.gray_r, interpolation='nearest')
plot.show()