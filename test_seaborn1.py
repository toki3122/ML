import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset("tips")
#sns.countplot(x='sex',data=df)
#sns.countplot(x='day',data=df)
#sns.barplot(x='total_bill',y='sex',data=df)
#sns.barplot(y='total_bill',x='smoker',data=df)
#sns.boxplot(x='smoker',y='total_bill',data=df)
#sns.boxplot(x='day',y='total_bill',data=df,palette='rainbow')
#sns.boxplot(y='day',x='total_bill',hue='smoker',data=df)
sns.violinplot(x="total_bill",y="day",data=df,palette='rainbow')
plt.show()