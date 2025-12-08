import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset("tips")
print(df.head())
#correlation heatmap is just to show 2D correlation matrix
print(df.corr(numeric_only=True))
sns.heatmap(df.corr(numeric_only=True))
sns.jointplot(x='tip',y='total_bill',data=df,kind='hex')#2d corralation plot between tip and total bill
#if we use reg as kind, we'll get a fitted curve using regression
sns.jointplot(x='tip',y='total_bill',data=df,kind='reg')
sns.pairplot(df,hue='sex')
sns.displot(df['tip'],kde=True)
plt.show()