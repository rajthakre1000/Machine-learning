import pandas as pd
import numpy as np

import scipy.stats as stats

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier             # no effect after transfomation

from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer

df = pd.read_csv(r'Titanic-Dataset.csv', usecols=(['Age', 'Fare', 'Survived']))
print(df.head())

# print(df.isnull().sum())
df['Age'].fillna(df['Age'].mean(), inplace= True)
# print(df.isnull().sum())

x = df[['Age', 'Fare']]
y = df['Survived']
print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=.2)
# checking if data is normal or not
plt.figure(figsize=(14,4))
plt.subplot(121)
sns.displot(x_train['Age'])
plt.title('Age PDF')

plt.subplot(122)
stats.probplot(x_train['Age'], dist="norm", plot=plt)
plt.title("Age QQ plot")

plt.show()

plt.subplot(121)
sns.displot(x_train['Fare'])
plt.title('Fare PDF')

plt.subplot(122)
stats.probplot(x_train['Fare'], dist="norm", plot=plt)
plt.title("Fare QQ plot")

plt.show()

clf1 = LogisticRegression()
clf2 = DecisionTreeClassifier()

clf1.fit(x_train, y_train)
clf2.fit(x_train, y_train)

y_pred1 = clf1.predict(x_test)
y_pred2 = clf2.predict(x_test)

print("Accuracy Logistic Regression:", accuracy_score(y_test, y_pred1))
print("Accuracy Decision Tree:", accuracy_score(y_test, y_pred2))

trf= FunctionTransformer(func= np.log1p)            #Custom function (log)
x_train_transformed = trf.fit_transform(x_train)
x_test_transformed = trf.fit_transform(x_test)

clf1.fit(x_train_transformed , y_train)
clf2.fit(x_train_transformed, y_train)

y_pred1 = clf1.predict(x_test_transformed)
y_pred2 = clf2.predict(x_test_transformed)
print("Accuracy after log by LR " , accuracy_score( y_test, y_pred1)*100 )
print("Accuracy after log by DT " ,accuracy_score( y_test,y_pred2)*100)

# cross validation
x_trandformed = trf.fit_transform(x)
clf1 = LogisticRegression()
clf2 = DecisionTreeClassifier()

print("LR ",np.mean(cross_val_score(clf1, x_trandformed, y, scoring='accuracy', cv=10))*100)        #train 10 times and gives average accuracy
print("DT ",np.mean(cross_val_score(clf2, x_trandformed, y, scoring='accuracy', cv=10))*100)        #train 10 times and gives average accuracy

# Fare
# plt.subplot(121)
# stats.probplot(x_train['Fare'], dist="norm", plot=plt)
# plt.title('Fare Before Log')
# plt.subplot(122)
# stats.probplot(x_train_transformed['Fare'], dist="norm", plot=plt)
# plt.title('Fare After Log')
# plt.show()

# Age
# plt.subplot(121)
# stats.probplot(x_train['Age'], dist="norm", plot=plt)
# plt.title('Age Before Log')
# plt.subplot(122)
# stats.probplot(x_train_transformed['Age'], dist="norm", plot=plt)
# plt.title('Age After Log')
# plt.show()
# result is getting worse when use log transorm on age

trf2 = ColumnTransformer([('log', FunctionTransformer(np.log1p),['Fare'])], remainder='passthrough')    # calling funcriontranformer and column is Fare, passthrough (age as is it)
x_train_transformed2 = trf2.fit_transform(x_train)
x_test_transformed2 =  trf2.transform(x_test)

clf1.fit(x_train_transformed2, y_train)
clf2.fit(x_train_transformed2, y_train)

y_pred = clf1.predict(x_test_transformed2)
y_pred2 = clf2.predict(x_test_transformed2)

# print("Accuracy with LG ", accuracy_score(y_test, y_pred))
# print("Accuracy with DT ", accuracy_score(y_test, y_pred2))


x_trandformed = trf2.fit_transform(x)
clf1 = LogisticRegression()
clf2 = DecisionTreeClassifier()

print("LR ",np.mean(cross_val_score(clf1, x_trandformed, y, scoring='accuracy', cv=10))*100)         
print("DT ",np.mean(cross_val_score(clf2, x_trandformed, y, scoring='accuracy', cv=10))*100)        
