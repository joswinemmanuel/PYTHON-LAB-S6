import numpy as np

# ways to make array

a = np.arange(10)
print(a)
# [0 1 2 3 4 5 6 7 8 9]

# 0D array
a = np.array(1)
print(a)
1

# 1D array
a = np.array([1, 2, 3])
print(a)
# [1 2 3]

# 2D array
a = np.array(([1, 2, 3], [4, 5, 6]))
print(a)
'''
[[1 2 3]
 [4 5 6]]
'''
# 3D array
a = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(a)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

a = np.array([1, 2, 3])
print(a)
# [1 2 3]

b = a + 1
print(b)
# [2 3 4]

c = a*2
print(c)
# [2 4 6]

d = 2**a
print(d)
# [2 4 8]
