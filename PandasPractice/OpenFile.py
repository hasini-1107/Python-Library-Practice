import pandas as pd
# opening the file
toyota = pd.read_csv("Toyota.csv", index_col=0)
# creating a deep copy
cars_data = toyota.copy(deep=True)

# to get row index
print(cars_data.index)
# to print all column labels
print(cars_data.columns)

# size of csv file
print(cars_data.size)

# memory usage
print(cars_data.memory_usage())

# selecting and indexing
print(cars_data.loc[:, 'FuelType'])
