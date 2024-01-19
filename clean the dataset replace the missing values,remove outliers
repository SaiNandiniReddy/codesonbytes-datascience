#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


x=pd.read_csv("netflix1.csv")
x


# In[5]:


x['date_added']=pd.to_datetime(x['date_added'],format='%m/%d/%Y')


# In[6]:


x['date_added']=pd.to_datetime(x['date_added'],format='%d-%m-%Y')


# In[7]:


x['date added']=x['date_added'].dt.strftime('%d-%m-%Y')
x


# In[8]:


x.type.value_counts()


# In[9]:


sns.countplot(x='type',data=x)
plt.title("count VS Type of Shows")


# In[10]:


x['country'].value_counts().head(10)


# In[34]:


plt.figure(figsize=(12,6))
sns.countplot(y='country',order=x['country'].value_counts().index[0:10],data=x)
plt.title('country wise content on Netflix')


# In[35]:


movie_countries=x[x['type']=='Movie']
tv_show_countries=x[x['type']=='Tv Show']
plt.figure(figsize=(12,6))
sns.countplot(y='country',order=x['country'].value_counts().index[0:20],data=movie_countries)
plt.title('Top 10 countries producing movies on Netflix')


# In[37]:


x.rating.value_counts()


# In[39]:


plt.figure(figsize=(10,6))
sns.countplot(x='rating',order=x['rating'].value_counts().index[0:10],data=x)
plt.title('Rating of Shows on Netflix VS Count')


# In[40]:


x.release_year.value_counts()[:20]


# In[41]:


plt.figure(figsize=(9,6))
sns.countplot(x='release_year',order=x['release_year'].value_counts().index[0:20],data=x)
plt.title('Content Release in years on Netflix VS Count')


# In[42]:


plt.figure(figsize=(12,8))
sns.countplot(y='listed_in',order=x['listed_in'].value_counts().index[0:20],data=x)
plt.title('Top 20 Genre on Netflix')


# In[ ]:




