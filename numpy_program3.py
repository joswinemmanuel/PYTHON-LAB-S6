import numpy as np

a = np.array([[2, 4], [5, -6]])
print(a)

b = np.array([[9, -3], [3, 6]])
print(b)

print(a.transpose())
'''
[[ 2  5]
 [ 4 -6]]
'''

print(b.T)
'''
[[ 9  3]
 [-3  6]]
'''


# Matrix Multiplication

print(a.dot(b))
'''
[[ 30  18]
 [ 27 -51]]
'''

#OR

print(np.matmul(a, b))
'''
[[ 30  18]
 [ 27 -51]]
'''

print(np.trace(a))
# -4

print(np.linalg.det(a))
# -32.0
