#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing the modules
import pandas as pd
import numpy as np


# In[5]:


#reading the data set into data
data=pd.read_csv("glass.csv")


# #Used to get the top 5 rows of the data set

# In[6]:


data.head()


# #Used to get the count, data_typ,column names,memory usage

# In[7]:


data.info()


# #Used to get the mean,min,max,no of rows(count),standard deviation,25,50,75 percentiles of numerical data type

# In[ ]:


data.describe()


# #dropping the target variable from the data set

# In[14]:


x=data.drop(["Type"],axis=1)
x.info()


# #appending the target variable to the y

# In[16]:


y=data["Type"]
y.head()


# #Importing SVC

# In[17]:


from sklearn.svm import SVC, LinearSVC


# #importing train_test_split to divide the data with train data (70%) and test data(30%)

# In[31]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
x_train.info()
x_test.info()
y_train.describe()


# #importing Gaussian Naive Bayes, Metrics is used for getting the accuracy scores

# In[41]:


from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import accuracy_score


# #train with Gaussian
# 

# In[42]:


gnb = GaussianNB()


# #Predict y by fittig the data with gaussian

# In[43]:


y_pred = gnb.fit(x_train, y_train).predict(x_test)


# #Accuracy scores

# In[44]:


accsrcore=accuracy_score(y_test,y_pred)
accsrcore


# In[45]:


# classification report


# In[46]:


print(metrics.classification_report(y_test,y_pred))


# #same is followed for Supoort vector machine

# In[47]:


svc = SVC()
svc.fit(x_train, y_train)
y_pred = svc.predict(x_test)
accscore=accuracy_score(y_test,y_pred)
accscore


# In[40]:


print(metrics.classification_report(y_test,y_pred))


# #For the classification problem, best score is 100% accuracy
# #For Regression problem, best score is 0% error
# #Accuracy score for GNB=0.5116279069767442 and Accuracy score for svc=0.4186046511627907
# #For this data set GNB has the best accuracy score

# In[ ]:




