import numpy as np
rng = np.random.default_rng(seed=1)  # seed is used to reproduce same output
print(rng.integers(1, 100, size=(3, 2)))  # low ,high ,no of ele
np.random.seed(seed=1)
print(np.random.uniform(low=-1, high=1, size=3))  # random used for float
array = np.array([1, 2, 3, 4])
rng.shuffle(array)
print(array)
