import pandas as pd

toyota = pd.read_csv("Toyota.csv", index_col=0, na_values=['??', '????'])
cars_data = toyota.copy(deep=True)
print(cars_data.info())

# converting dataTypes
cars_data['Automatic'] = cars_data['Automatic'].astype('object')

# object vs category
print(cars_data['FuelType'].memory_usage())
cars_data['FuelType'] = cars_data['FuelType'].astype('category')
print(cars_data['FuelType'].memory_usage())


# detect null values
print(cars_data.isnull().sum())
