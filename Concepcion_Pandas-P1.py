#!/usr/bin/env python
# coding: utf-8

# # PROBLEM 1: Using knowledge obtained from the experiment and demonstrations:
#  

# # a. Load the corresponding .csv file into a data frame named cars using pandas

# In[3]:


import pandas as pd

# Load the CSV file into a DataFrame
cars = pd.read_csv("cars.csv")

# Display the data coming from cars.csv
cars


# # b. Display the first five and last five rows of the resulting cars.

# In[13]:


import pandas as pd

# Load the CSV file into a DataFrame
cars = pd.read_csv('cars.csv')

# Use the head() method to show the first five rows
first_five = cars.head()
#To print the first five rows of the resulting cars
first_five


# In[15]:


# Use the tail() method to show the first five rows
last_five = cars.tail()
# To print the last five rows of the resulting cars
last_five


# In[ ]:




