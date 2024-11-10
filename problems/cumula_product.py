#Cumulative Sum and Product
import numpy as np

# Creating an array
arr = np.array([11, 12, 13, 14])

# Calculating cumulative sum and product
cumulative_sum = np.cumsum(arr)
cumulative_product = np.cumprod(arr)

print('Cumulative Sum:', cumulative_sum)
print('Cumulative Product:', cumulative_product)