# Advanced Indexing with Meshgrid
import numpy as np

# Creating 1D arrays
x = np.array([1, 6, 3])
y = np.array([2, 9])

# Creating meshgrid for advanced indexing
X, Y = np.meshgrid(x, y)
indices = np.vstack([X.ravel(), Y.ravel()])

print('Indices for Meshgrid Advanced Indexing:\n', indices)