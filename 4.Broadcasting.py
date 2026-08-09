# Boardcasting allows numpy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match a larger arrays shape
import numpy as np
arr1 = np.array([[1, 2, 3]])  # shape = 1,3
arr2 = np.array([[1], [2], [3]])  # must consist of 1 ie shape = 3,1
print(arr1.shape)
print(arr2.shape)
print(arr1*arr2)
