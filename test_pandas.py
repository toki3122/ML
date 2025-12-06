import pandas as pd
import numpy as np
df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'],columns=["Column1","Column2","Column3","Column4"])#dataframe init
print(df.head())
df.to_csv('test1.csv')
#accessing teh elements: 1.location(.loc) 2.index location(.iloc)
print(df.loc['Row1'])
print(type(df.loc['Row1']))#<class 'pandas.core.series.Series'>
#but for iloc it will be data frame, unless it has one column
print(df.iloc[0:2,0:2])
print(type(df.iloc[0:2,0:2]))
#converting data frames into arrays:
print(df.iloc[:,1:].values)
#nullcheck:
print(df.isnull().sum())
print(df['Column1'].value_counts())
print(df['Column1'].unique())
print(df[['Column3','Column4']])
