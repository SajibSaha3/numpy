#Boolean Indexing 1
import numpy as np

# Creating an array
array = np.array([2, 41, 6, 8, 11, 12])

# Boolean indexing
even_numbers = array[array % 2 != 0]

print('Original Array:', array)
print(f'The boolean value is the {even_numbers}')