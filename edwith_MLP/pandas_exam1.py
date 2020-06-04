import pandas as pd

data_url= 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'

df_data = pd.read_csv(data_url, sep='\s+', header = None)

print(df_data.head())
