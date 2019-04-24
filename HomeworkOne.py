#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
data = pd.read_csv('Data_Entry_2017.csv')


# In[5]:


data.head()


# In[10]:


data.index.values


# In[12]:


data


# In[13]:


data.groupby('Finding Labels')['Follow-up #'].mean()


# In[14]:


b = data.set_index('Patient Age')
b.head()


# In[15]:


b


# In[21]:


data.describe()


# In[22]:


b.describe()


# In[ ]:




