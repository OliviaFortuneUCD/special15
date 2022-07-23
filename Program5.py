#importing libraries
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

df=pd.read_csv("train.csv")
df_t=pd.read_csv("test.csv")

print(df.shape)
print(df_t.shape)

plt.figure(figsize=(25, 25))
for i, col in enumerate(df.select_dtypes(include=['float64']).columns):
    ax = plt.subplot(11,4, i+1)
    sns.histplot(data=df, x=col, ax=ax)
plt.suptitle('Histogram Plots for all continuous variables')
plt.tight_layout()

plt.figure(figsize=(25, 25))
for i, col in enumerate(df.select_dtypes(include=['int64']).columns):
    ax = plt.subplot(11,4, i+1)
    sns.histplot(data=df, x=col, ax=ax)
plt.suptitle('Histogram Plots for all continuous variables')
plt.tight_layout()