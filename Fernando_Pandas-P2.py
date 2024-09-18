#!/usr/bin/env python
# coding: utf-8

# # Problem 2: Using the dataframe `cars` from Problem 1, extract the following information using subsetting, slicing, and indexing operations:

# ##### Loading the cars.csv file 

# In[5]:


import pandas as pd

#load `cars.csv` file into a data frame named cars using pandas.
cars = pd.read_csv('cars.csv')
cars


# ##### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.

# In[8]:


#Display the first five rows of the `cars` data frame, selecting every second row starting from index 1.
cars[1::2].head()


# ##### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# In[11]:


#Retrieve the 'Model' column for the first row (index 0) of the `cars` data frame.
cars.loc[[0], ['Model']]


# ##### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have? 

# In[14]:


#Calling the 'Model' and 'cyl' columns for the row at index 23 of the `cars` data frame.
cars.loc[[23], ['Model', 'cyl']]


# ##### d. Determine how many cylinders (cyl) and what gear type (gear) do the car models Mazda RX4 Wag, Ford Pantera L, and Honda Civic have.
#  

# In[17]:


#Retrieve the 'Model', 'cyl', and 'gear' columns for the rows at indices 1, 28, and 18 of the `cars` data frame.
cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]


# In[ ]:




