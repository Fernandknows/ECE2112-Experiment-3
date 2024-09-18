#!/usr/bin/env python
# coding: utf-8

# ## Problem 1: Using knowledge obtained from the experiment and demonstrations

# ##### a. Load the corresponding .csv file into a data frame named cars using pandas 

# In[1]:


import pandas as pd

#load cars.csv file into a data frame named cars using pandas.
cars = pd.read_csv('cars.csv')
cars


# ##### b. Display the first five and last five rows of the resulting cars.

# In[6]:


#Display the first five rows of the resulting cars.
cars.head()

#Display the last five rows of the resulting cars.
cars.tail()


# In[ ]:




