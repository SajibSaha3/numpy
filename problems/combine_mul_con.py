import numpy as np

# Creating a 2D array
arr = np.array([[15, 20, 25], [42, 49, 55], [71, 68, 66]])

# Get rows where any element is greater than 30
rows_with_values_gt_30 = (arr > 30).any(axis=1)

# Select those rows and specific columns (0 and 2)
result = arr[rows_with_values_gt_30][:, [0, 2]]

print('Combined Indexing Result:', result)
