#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd


# In[ ]:


#read the input file


# In[48]:


data = pd.read_csv("Icp5task1.csv") 


# In[ ]:


#To get the information


# In[11]:


data.info()


# In[ ]:


#to describe the data


# In[12]:


data.describe()


# In[13]:


data.head()


# In[16]:


#importing matplotlib for scatterplot
import matplotlib.pyplot as plt


# In[45]:


#scatterplot size 
plt.figure(figsize=(10,8))
#scatterplot for GarageArea taken on x-axis,SalePrice taken as y axis with red color
plt.scatter(data.GarageArea,data.SalePrice,s=30,color='r')
#title of the plot
plt.title("Anomalies in GaurageArea field and SalePrice")
#X axis label of the plot
plt.xlabel('GarageArea')
#Y axis label of the plot
plt.ylabel('SalePrice')
# shows the scatter plot
plt.show()


# In[ ]:


# ramoved the rows with GarageArea less than or equal to 180,GarageArea greater than or equal to 1000 and GarageArea greater than or equal to 500000


# In[41]:


non_out_data=data[ (data.GarageArea > 180) &(data.GarageArea <1000) & (data.SalePrice <500000) ]


# In[42]:


non_out_data.describe()


# In[ ]:


#scatter plot after removing the Anomalies from GaurageArea field and SalePrice


# In[46]:


plt.figure(figsize=(10,8))
plt.scatter(non_out_data.GarageArea,non_out_data.SalePrice,s=30,color='blue')
plt.title("Anomalies removed from GaurageArea field and SalePrice")
plt.xlabel('GarageArea')
plt.ylabel('SalePrice')
plt.show()


# In[ ]:





# In[ ]:




