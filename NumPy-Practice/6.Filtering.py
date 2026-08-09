import numpy as np
ages = np.array([[1, 2, 34, 4], [4, 5, 6, 7]])
kids = np.where(ages < 4, ages, 0)
print(kids)
# where is used to prevese original size
