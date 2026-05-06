import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
print(df.head())#prints first 5 rows
print(df.shape)
####################
#univariate analysis
####################
df_setosa=df.loc[df['species']=='setosa']
print(df_setosa)#print all the rows having setosa species
df_virginica=df.loc[df['species']=='virginica']
print(df_virginica)#print all the rows having virginica species
df_versicolor=df.loc[df['species']=='versicolor']
print(df_versicolor)#print all the rows having versicolor species
plt.plot(df_setosa['sepal_width'],np.zeros_like(df_setosa['sepal_width']))
plt.plot(df_virginica['sepal_width'],np.zeros_like(df_virginica['sepal_width']))
plt.plot(df_versicolor['sepal_width'],np.zeros_like(df_versicolor['sepal_width']))
plt.show()
#the plot will show three types, but as there is only one data(sepal length),
#it just distributes itself on x axis but the y axis values will be zero

###################
#bivariate analysis
###################

#taking 2 datas to plot(sepal length and sepal width)
sns.FacetGrid(df,hue="species").map(plt.scatter,"sepal_length","sepal_width").add_legend()
plt.show()

######################
#multivariate analysis
######################

sns.pairplot(df,hue="species")
plt.show()