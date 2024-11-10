# Conditional Indexing
import numpy as np

# Creating an array
arr = np.array([1, 2, 3, 4, 5, 6])

# Setting elements that satisfy a condition
arr[arr % 2 != 0] = 0  # Set even numbers to -1

print('Array after Conditional Indexing:', arr)