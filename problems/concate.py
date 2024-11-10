# Concatenation of Arrays
import numpy as np

# Creating arrays
arr1 = np.array([1,3,5,7])
arr2 = np.array([2,4,6,8])

# Concatenating arrays
new_arr = np.concatenate((arr1, arr2))

print('array after concatenation:', new_arr)