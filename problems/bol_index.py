# Boolean Indexing
import numpy as np

# Creating an array
array = np.array([10, 15, 20, 25, 30])

# Boolean indexing
find_greater = array[array > 25]

print('Elements Greater Than 25:', find_greater)