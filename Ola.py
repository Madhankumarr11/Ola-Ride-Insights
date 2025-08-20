import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ola = pd.read_excel('D:/SRMK/Guvi/Ola-Ride-Insights/OLA_DataSet.xlsx')

# print("shape", ola.shape)

# print(ola.info())

# print(ola.describe())

# print(ola.isnull().sum())

# print((ola.isnull().sum() / len(ola))*100)

sns.boxplot(x=['ola'])







