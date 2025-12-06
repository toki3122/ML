import pandas as pd
import numpy as np
from io import StringIO, BytesIO
#opening and reading csv files
df=pd.read_csv('F:\\tokee\\programming\\python\\machine_learning\\mercedesbenz.csv')
print(df.head())#writing
print("")
print(df.info())
print("")
print(df.describe())#overall description
print("")
print(df['X0'].value_counts())#unique category count
print("")
data=('col1,col2,col3\n''x,y,z\n''a,b,2\n''c,d,3\n')
print("")
print(type(data))#returns string
print("")
print(pd.read_csv(StringIO(data)))#turns the string into a dataset and read as a csv
#to read from specific columns:
df=pd.read_csv(StringIO(data), usecols=['col1','col3'])
print("")
print(df.head())
print("")
df.to_csv('F:\\tokee\\programming\\python\\machine_learning\\test.csv')#transports the dataset to a csv file
data=('a,b,c,d\n''0,1,2,3\n''5,6,7,8\n''9,10,11\n')
print(data)
print("")
df=pd.read_csv(StringIO(data),dtype=object)#dtype is object otherwise we get ValueError: Integer column has NA values in column 3
print(df)
print("")
print(df['a'])
df=pd.read_csv(StringIO(data),dtype={'b':int, 'c':float,'a':'int64'})
print(df)
print(df.dtypes)
print("")
data=('index,a,b,c\n''0,1,2,3.141\n''5,6,7,8\n')
df=pd.read_csv(StringIO(data),index_col=0)#makes the default index column disappear
print(df)
data=('a,b,c\n''4,apple,bat,\n''8,orange,cow,')
#the first column turns into index and c is nan nan
df=pd.read_csv(StringIO(data))
print(df)
#to fix it:
df=pd.read_csv(StringIO(data),index_col=False)
print(df)
data=('a,b\n"hello, \\"bob\\",nice to see you",5')
df=pd.read_csv(StringIO(data),escapechar='\\')
print(df)
#df=pd.read_csv('https://download.bis.gov/pub/time.series/cu/cu.item',sep='\t')
#print(df)