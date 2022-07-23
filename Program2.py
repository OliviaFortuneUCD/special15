import pandas as pd ## pandas is used to manupulate the dataframe
import numpy as np ## numpy is used to do scientific calculations
import matplotlib.pyplot as plt ## matplotlib used for visualization
import seaborn as sns ## seaborn used for visualization
import missingno as msno ## used to visualize missing values
import warnings ## used to remove warnings
warnings.filterwarnings('ignore')

## Importing the data

data=pd.read_csv('Train.csv')

print(data.head())
print(data.info())


pd.options.display.max_rows=None ## shows all the rows
data.isnull().sum()

plt.figure(figsize=(25,15))
sns.heatmap(data.drop('SalePrice',axis=1).corr(),cmap="BuPu",annot=True)
plt.show()