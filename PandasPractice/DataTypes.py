import pandas as pd

toyota = pd.read_csv("Toyota.csv", index_col=0)

cars_data = toyota.copy(deep=True)
# returns data types of each column
print(cars_data.dtypes)

# number of columns for each data type
print(cars_data.dtypes.value_counts())

# checking format of each column
print(cars_data.info())

# unique elements
print(cars_data['FuelType'].unique())
