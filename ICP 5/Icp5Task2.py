#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("winequality-red.csv") 


# In[3]:


data.info()


# In[4]:


data.describe()


# In[22]:


# detect the missing values 
data.isna()


# In[23]:


data.isna().sum()


# In[ ]:


#correlation of all the features variables with the target label(quality)


# In[21]:


data[data.columns[1:]].corr()['quality'][:-1]


# In[17]:


corr_data=data.corr()


# In[ ]:


# plotting the heat map with seaborn and matplotlib


# In[19]:


# for plotting the heat map
import seaborn as sn
import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))
sn.heatmap(corr_data, annot=True)
plt.show()


# In[46]:


#Correlation with output variable
cor_target = abs(corr_data["quality"])
# getting the high correlated values whose absoolute values are >0.2 and removing the last column
relevant_features = cor_target[cor_target>0.2][:-1]
#Selecting the top 3 relavent values 
relevant_features.sort_values(kind="quicksort",ascending=False)[:]


# In[49]:


#getting the feature varibales as one data set and target variable into other data set
X = data[['alcohol','volatile acidity','sulphates']]
X.info()


# In[48]:


y=data[['quality']]
y.head()


# In[50]:


#imported train_test_split for dividing the data 
from sklearn.model_selection import train_test_split
#dividing the 30% of data to test and remaining to train
X_train, X_test, y_train, y_test = train_test_split(
                                    X, y, random_state=42, test_size=.30)
X_train.info()


# In[52]:


#As multiple linear regression is extension of linear regression, fit the data into linear_model
from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)
##Evaluate the performance and visualize results
#R^2 score
print ("R^2 is : ", model.score(X_test, y_test))
predictions = model.predict(X_test)
#RMSE score
from sklearn.metrics import mean_squared_error
print ('RMSE is :', mean_squared_error(y_test, predictions))


# In[ ]:




