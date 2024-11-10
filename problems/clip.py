#Clipping Array Values
import numpy as np

# Creating an array
array = np.array([6,5,7,9,1,2])

# Clipping values to be between 1 and 4
clipped_array = np.clip(array, 1, 4)

print('Original Array:', array)
print('Clipped Array:', clipped_array)