import pandas as pd

ola = pd.read_excel('D:/SRMK/Guvi/Ola-Ride-Insights/OLA_DataSet.xlsx')

# print("shape", ola.shape)

# print(ola.info())

# print(ola.describe())

# print(ola.isnull().sum())

print((ola.isnull().sum() / len(ola))*100)







