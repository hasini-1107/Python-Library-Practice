import numpy as np
array = np.array([1, 2, 3])
print(array.ndim)  # prints number of dimensions in an array
array = np.array([[[1, 2, 3], [3, 4, 5], [2, 3, 4]],
                  [[1, 2, 3], [3, 4, 5], [2, "", 4]]])
print(array.ndim)
print(array.shape)  # gives a tuple(depth,no of rows,no of columns in each row)
print(array[1][1][1])
print(array[1, 1, 1])  # both give same result

word = array[0, 0, 0] + array[1, 2, 0] + array[1, 0, 0]
print(word)
