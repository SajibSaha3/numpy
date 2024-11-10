# Using Ellipsis (...) in Indexing
import numpy as np

# Creating a 3D array
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# Using ellipsis to select all elements along specific axes
values = arr[..., 0]  # Selecting the second column in each 2D slice

print('the values are the :--', values)