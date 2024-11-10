# Combining Boolean and Fancy Indexing
import numpy as np

# Creating an array
new_arr = np.array([10, 15, 20, 25, 30])

# Boolean condition combined with specific indices
final = new_arr[(new_arr > 15) & (new_arr <= 30)][[0, 2]]

print('Combined Boolean and Fancy Indexing Result:', final)