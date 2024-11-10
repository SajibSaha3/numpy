import numpy as np

array = np.array([0, 1, 2, 0])
choices = array ** 2
# Using np.choose to select based on values in `array`
result = np.choose(array, choices)

print(result)
