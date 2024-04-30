import numpy as np

a = np.array([[2, 4], [5, -6]])
print(a)

b = np.array([[9, -3], [3, 6]])
print(b)

c = a + b
print(c)
'''
[[11  1]
 [ 8  0]]
'''

c = a - b
print(c)
'''
[[ -7   7]
 [  2 -12]]
'''

c = a * b
print(c)
'''
[[ 18 -12]
 [ 15 -36]]
'''
