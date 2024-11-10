#Basic Arithmetic Operations
import numpy as np

# Creating arrays
array1 = np.array([9, 8, 7])
array2 = np.array([4, 5, 9])

# Arithmetic operations
added = np.add(array1, array2)
subtracted = np.subtract(array1, array2)
multiplied = np.multiply(array1, array2)
divided = np.divide(array1, array2)

print('Value of addition is----:', added)
print(' value of Subtracted is ---:', subtracted)
print(f'the value of the multiplied is {multiplied}')
print('Divided:', divided)