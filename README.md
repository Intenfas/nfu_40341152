MIN_YUE TEST
=========================
#一般的向量相加，但會變成矩陣串列
x = [13, 2, 5]
y = [1, 9, 12]
print x + y
x+y = [13, 2, 5, 1, 9, 12]
#使用numpy 可以簡易使用向量運算
import numpy as np

a = np.array([12, 21, 34])
b = np.array([25, 44, 63])
print a + b
a+b= [37 65 97]

#使用numpy 計算角度公式
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


# 第三個範例

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