#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
df=pd.read_csv("Downloads/assignment2.csv")
df


# In[2]:


df.isnull()


# In[3]:


series=pd.isnull(df['Math_Score'])
df[series]


# In[5]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Gender']=le.fit_transform(df['Gender'])
newdf=df
df


# In[6]:


missing_values=['Na','na']
df=pd.read_csv("Downloads/assignment2.csv",na_values=missing_values)
df


# In[7]:


ndf=df
df.fillna(0)


# In[9]:


df['Math_Score']=df['Math_Score'].fillna(df['Math_Score'].mean())
df


# In[10]:


m_v=df['Math_Score'].mean()
df['Math_Score'].fillna(value=m_v, inplace=True)
df


# In[11]:


ndf.replace(to_replace = np.nan, value = -99)


# In[12]:


ndf.dropna()


# In[13]:


from scipy import stats


# In[14]:


z = np.abs(stats.zscore(df['Math_Score']))
z


# In[ ]:




