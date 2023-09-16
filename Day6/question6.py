# 7) Write a NumPy program to create an array with the values 1, 7, 13, 105 and
# determine the size of the memory occupied by the array.
import numpy as np

y = np.array([12, 34, 56, 78, 90])
print(f"original array{y}")
print(f"the size of numpy array{y.size,}\nmemory size:{y.nbytes} in bytes")
print(f"item size of y array ={y.itemsize}")
