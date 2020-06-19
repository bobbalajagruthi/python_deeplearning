#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# #Reading the CSV file

# In[5]:


data = pd.read_csv("train_preprocessed.csv") 


# #Used to get the top 5 rows of the data set

# In[6]:


data.head()


# #Used to get the count, data_typ,column names,memory usage

# In[7]:


data.info()


# #Used to get the mean,min,max,no of rows(count),standard deviation,25,50,75 percentiles of numerical data type

# In[8]:


data.describe()


# #Used to get the correlation of the data set

# In[17]:


data_corr=data.corr()


# ##Used to get the correlation of the data set with respect to "Survived" column

# In[29]:


y=data_corr["Survived"]


# #Used to get the correlation of the data set with respect to "Sex" column

# In[19]:


data_corr["Sex"]


# #Used to get the correlation between "Survived" and "Sex"column

# In[24]:


data["Sex"].corr(data["Survived"])


# #Values which are greater than 0.3 and less than -0.3 are considered as significant

# #As the value is greater than 0.3 we need to put consider this feature

# In[ ]:




