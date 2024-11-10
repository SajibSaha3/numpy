import numpy as np

# Creating an array with valid indices for choices
array = np.array([0, 1, 2, 0])  # Modified to avoid 3, which is out of bounds

# Defining choices
choices = [array * 2, array + 5, array ** 3]

# Using np.choose
result = np.choose(array, choices)
print('Result using np.choose:', result)

