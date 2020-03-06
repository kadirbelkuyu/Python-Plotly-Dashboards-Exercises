import pandas as pd
import numpy as np

data = pd.read_csv('../../data/salaries.csv')
print(data)

print(data['Name'])
print(data['Salary'])

print(data['Name', 'Salary'])

print(data['Age'].mean())

ser_of_bool = data['Age'] > 30
print(ser_of_bool)

age_filter = data['Age'] > 30
print(age_filter)

data[data['Age'] > 30]

data['Age'].unique() # list of unique values for Age
data['Age'].nunique() # number of unqiue values
data.info() # General info about your dataframe
data.describe() # Statistics about your dataframe
data.columns # Grab a list of all columns
data.index # Create an index list

mat = np.arange(50).reshape(5,10)