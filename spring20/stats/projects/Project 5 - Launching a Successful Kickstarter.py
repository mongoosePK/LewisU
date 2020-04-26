#!/usr/bin/env python
# coding: utf-8

# ## Project 5: Launching a Successful Kickstarter

# In[1]:


# Imports pandas, which lets us use Data Frames. 
import pandas as pd

# Imports plotting functionality.
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

# We need this for our simulations. 
import numpy as np
import scipy.stats as stats


# In[2]:


# Imports our data from 'train.csv' in the 'data' folder. 
kickstarters = pd.read_csv('data/kickstarter.csv')

# .head(10) shows the first ten entries of a data frame by default. 
kickstarters.head(10)


# In[3]:


columns_to_change = {'backers', 'usd pledged'}
for col in columns_to_change:
    kickstarters[col] = pd.to_numeric(kickstarters[col], errors='coerce')
    
del kickstarters['Unnamed: 5']
del kickstarters['Unnamed: 6']
del kickstarters['Unnamed: 7']
del kickstarters['Unnamed: 8']

#kickstarters.dropna(inplace=True)


# In[4]:


# Question 1 - Pick a category from the below list that sounds interesting to you!
kickstarters['category'].value_counts().head(15)


# In[5]:


# Question 2 - Change the category to the one you chose!
my_category = kickstarters[kickstarters.category == 'Fiction']
len(my_category)


# In[6]:


numerator = len(my_category[my_category.state == 'successful'])


# In[7]:


# Question 3
numerator/len(my_category)


# In[8]:


# Set-up for Question 4
my_category['state'].value_counts()


# In[ ]:




