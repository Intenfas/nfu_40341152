MIN_YUE TEST
=========================


# 一般的向量相加，但會變成矩陣串列

x = [13, 2, 5]
y = [1, 9, 12]
print x + y
x+y = [13, 2, 5, 1, 9, 12]

# 使用numpy 可以簡易使用向量運算

import numpy as np

a = np.array([12, 21, 34])
b = np.array([25, 44, 63])
print a + b
a+b= [37 65 97]

# 使用numpy 計算角度公式

import numpy as np

a = np.array([21, 31, 24])
b = np.array([-22, 13, -15])

la = np.sqrt(a.dot(a))
lb = np.sqrt(b.dot(b))
print("----計算向量長度----")
print (la, lb)
la,lb = (44.474711915874174, 29.631064780058107)

cos_angle = a.dot(b) / (la * lb)
cos_angle = -0.317946187256

print("----計算cos ----")
print (cos_angle)

angle = np.arccos(cos_angle)


print("----計算夾角(單位為π)----")
print (angle)
angle = 1.89435880439


angle2 = angle * 360 / 2 / np.pi
print("----轉換單位為角度----")
print (angle2)
angle2 = 108.538764375


# 使用numpy 進行矩陣乘法運算

import numpy as np

a = np.array([[8, 8], [4, 6]])
b = np.array([[2, 4], [6, 8]])
c = np.mat([[6, 8], [4, 6]])
d = np.mat([[2, 4], [6, 8]])
e = np.dot(a, b)
f = np.dot(c, d)
print("----乘法運算----")
print (a * b)
print (c * d)
a*b =
[[ 3  8]
 [ 6 12]]
c*d =
[[15 22]
 [11 16]]

print("----矩陣相乘----")
print (e)
print (f)
print("----矩陣相乘----")

# 繪製圖表
import numpy as np
from matplotlib import pyplot
from numpy import *


a = mat([[1,2,-6],[3,10,8],[7,4,5]])
print linalg.det(a)
x = np.arange(0,10,0.2)
y = np.sin(x)
pyplot.plot(x,y)
pyplot.show()




# 使用pandas與Random作出亂數之散佈圖

import pandas as pd
%matplotlib inline
import random
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.DataFrame()

df['x'] = random.sample(range(0, 100), 30)
df['y'] = random.sample(range(0, 100), 30)
fig=sns.lmplot('x', 'y', data=df, fit_reg=False)
fig.savefig(“output.png”)
fig.plt.show()

# homework
# coding=utf-8
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from scipy.stats import norm
#例子一
fig = plt.gcf()
fig.set_size_inches(10,6)

var('x')
f = lambda x: exp(-x**2/2)

x = np.linspace(-5,6,200)
y = np.array([f(v) for v in x],dtype='float')

plt.grid(True)
plt.title('Gaussian Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,y,color='gray')
plt.fill_between(x,y,0,color='#c0f0c0')
plt.show()

#例子二
fig, ax = plt.subplots(1, 1)

x = np.linspace(norm.ppf(0.01),norm.ppf(0.99), 100)

ax.plot(x, norm.pdf(x),'r-', lw=50, alpha=0.6, label='norm pdf')

ax.plot(x, norm.pdf(x), 'k-', lw=20, label='frozen pdf')

r = norm.rvs(size=1000)

ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)

ax.legend(loc='best', frameon=False)

plt.show()