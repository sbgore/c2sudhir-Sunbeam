# 8) Write a NumPy program to convert an data type into to a floating type.
# a2 = np.array([10, 20, 30, 40, 50], dtype='float')
# print(a2.dtype)

import numpy as np

array = np.array(([10, 20, 30, 40, 50]))
print(f"original data type :{array.dtype}")
array = array.astype('float64')
print(array.dtype)
print(array)
# # array is immutable but how changed is data type after that print the float array
# array=np.array([10, 20, 30, 40, 50],dtype='float')
# print(array)