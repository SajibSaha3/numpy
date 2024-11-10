import numpy as np

# Creating a 3D array
array_3d = np.array([[[2, 12], [13, 14]], [[51, 61], [17, 81]]])

# Accessing elements in a 3D array
element = array_3d[1, 1, 1]  # Accessing the element at [1, 0, 1]

# Slicing in 3D
slice_3d = array_3d[1, 0, 1]

print('Element at (1,1,1):', element)
print('Sliced 3D Array:\n', slice_3d)