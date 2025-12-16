import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
train=pd.read_csv('F:\\tokee\\programming\\python\\machine_learning\\Titanic-Dataset.csv')
print(train.head())
print(train.isnull())
#sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')#shows missing values
#ML models cannot handle missing values, We must either fill or remove them
sns.set_style('whitegrid')
#sns.countplot(x='Survived',data=train)#survived and not survived
#sns.countplot(x='Survived',hue='Sex',data=train,palette='RdBu_r')#survived and not survived divided by sex
#sns.countplot(x='Survived',hue='Pclass',data=train,palette='rainbow')#divided by passenger class
#sns.displot(train['Age'].dropna(),kde=False,color='darkred',bins=40)#prints histogram for a different ages, where the missing values are not taken into account, with no kernel density(smooth density curve),and splited into 40 intervals
#sns.countplot(x='SibSp',data=train)#NUMBER OF SIBLINGS OR SPOUSE
#plt.figure(figsize=(12,7))#defines figure size
#sns.boxplot(x='Pclass',y='Age',data=train,palette='winter')
#puts average age onto the missing ages
def impute_age(cols):
    Age=cols[0]
    Pclass=cols[1]
    if pd.isnull(Age):
        if Pclass==1:
            return 37
        if Pclass==2:
            return 29
        else:
            return 24
    else:
        return Age
train['Age']=train[['Age','Pclass']].apply(impute_age,axis=1)
#null values are removed
#sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
#cabin still has nullvalues, too much null values to handle, so we just drop it 
train.drop('Cabin',axis=1,inplace=True)
plt.figure(figsize=(11,6))
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()
#data handling for sex and embark:
print(pd.get_dummies(train['Embarked'],drop_first=True).head())
sex=pd.get_dummies(train['Sex'],drop_first=True)
embark=pd.get_dummies(train['Embarked'],drop_first=True)
train.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
print(train.head())
train=pd.concat([train,sex,embark],axis=1)
print(train.head())
x_train,x_test,y_train,y_test=train_test_split(train.drop('Survived',axis=1),train['Survived'],test_size=0.30,random_state=101)
logmodel=LogisticRegression()
logmodel.fit(x_train,y_train)
predictions=logmodel.predict(x_test)
accuracy=confusion_matrix(y_test,predictions)
print(accuracy)
accuracy=accuracy_score(y_test,predictions)
print(accuracy)
print(predictions)