import numpy as np
# Scalar arithmetic
array = np.array([1, 2, 3])
print(array + 1)  # adds 1 to each element
print(array - 1)
print(array * 3)
print(array / 4)
print(array**2)

# Vectorized math func
array = np.array([4.1, 5.33, 6.45])
print(np.sqrt(array))  # squar root
print(np.round(array))  # round offs the numbers 4.1->4.
print(np.ceil(array))  # round of to higher num 4.1->4
print(np.pi)

radii = np.array([1, 2, 3])
print(np.pi*(radii**2))

# element-wise arithematic
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)

# Camparison operators
scores = np.array([90, 92, 93, 100, 98, 45, 67, 82])
print(scores >= 90)
scores[scores < 60] = 0
print(scores)
