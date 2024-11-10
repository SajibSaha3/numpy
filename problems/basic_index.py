# Basic Indexing and Slicing
import numpy as np

# Creating an array
array = np.arange(15)

# Accessing elements by index
first_element = array[0]
last_element = array[-1]
forth_element = array[3]

# Slicing the array
slice_array = array[2:6]

print('First Element:', first_element)
print('Last Element:', last_element)
print(f'value of 4th element is {forth_element}')
print('Sliced Array:', slice_array)