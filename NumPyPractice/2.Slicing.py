import numpy as np
array = np.array([[4, 4, 5, 12],
                  [11, 8, 7, 4],
                  [1, 2, 3, 41],
                  [6, 2, 0, 6]])

# array[start:end:step]

print(array[0:4:2])
print(array[::-1])  # reveresed
print(array[:, -1])  # all rows and last column
print(array[:, 1:3])  # print all rows and 1,2 columns
print(array[:, ::2])  # similar to array[0:4:2] but columns
print(array[1:3, 1:3])  # print rows 1,2 and columns 1,2
