# aggregate = summarize data and typically return a single value
import numpy as np
array = np.array([[1, 2, 3, 4], [4, 5, 6, 6]])
print(np.sum(array))
print(np.mean(array))
print(np.std(array))  # standard deviation
print(np.var(array))  # variance
print(np.min(array))
print(np.max(array))
print(np.argmin(array))  # position of max element
print(np.sum(array, axis=1))  # axis = 1 sum of each row
# axis = 0 addition of columns of rows
