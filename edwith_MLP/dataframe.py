from pandas import Series, DataFrame
import pandas as pd
import numpy as np

raw_data = { 'first_name' : ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
             'last_name' : ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
             'age' : [42, 52, 36, 24, 73],
             'city' : ['San Francisco', 'Baltimore', 'Miami', 'Douglas', 'Boston']}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'city'])
print(df)

print(DataFrame(raw_data, columns=['first_name', 'age']))

print(df.loc[1])

df_1 = DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'city', 'debt'])

print(df_1)

df_1.debt = df_1.age > 40

print(df_1)

print(df_1.values)

print(df_1.to_csv())

print(df['first_name'].head(2))

print(df[['first_name', 'last_name']].head(2))