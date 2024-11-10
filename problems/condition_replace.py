#Conditional Replacement with np.where
import numpy as np

# Creating an array
arr = np.array([15,20,10,5,25,30])

# Replacing values based on condition
values = np.where(arr > 20, 0, arr)

print('Array with Values Greater Than 20 Replaced with 0:', values)