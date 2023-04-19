#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install plotly')


# In[12]:


import pandas as pd
import plotly.express as px


# In[13]:


df = pd.read_csv("INFO 450/workout_data.csv")
df


# In[14]:


fig = px.bar(x=df["Maxpulse"], y=df["Calories"], color=df["Duration"])
fig.show()


# In[17]:


fig = px.treemap(df, path=[px.Constant("all"), 'Duration', 'Maxpulse'], values='Calories')
fig.show()


# In[20]:


fig = px.sunburst(df, path=['Duration', 'Pulse'], values='Calories')
fig.show()


# In[ ]:




