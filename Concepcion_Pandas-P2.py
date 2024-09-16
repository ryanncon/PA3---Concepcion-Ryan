#!/usr/bin/env python
# coding: utf-8

# # PROBLEM 2: Using the dataframe cars in problem 1, extract the following information using subsetting, slicing, and indexing operations.

# # a. Display the first five rows with odd-numbered columns (columns 1,3,5,7...) of cars.

# In[2]:


import pandas as pd
cars = pd.read_csv("cars.csv")


# In[3]:


# Display the first five rows with odd-numbered columns
odd_columns = cars.iloc[:5, ::2]  # Selects all rows and odd columns (index starts from 0)
print("First five rows with odd columns:")
odd_columns


# # b. Display the row that contains the 'Model' of 'Mazda RX4'

# In[5]:


# Display the row containing the model 'Mazda RX4'
mazda_rx4 = cars[cars['Model'] == 'Mazda RX4']
print("Mazda RX4 row:")
mazda_rx4


# # c. How many cylinders ('cyl') does the car model 'Camaro Z28' have?

# In[8]:


# Filter the row for 'Camaro Z28' and extract relevant information
camaro_z28_data = cars[cars['Model'] == 'Camaro Z28'][['Model', 'cyl']]

# To display how many cylinders does the car model 'Camaro Z28' have
camaro_z28 = pd.DataFrame(camaro_z28_data)

# Display the table
camaro_z28


# # d. How many cylinders ('cyl') and what gear type ('gear') do the car models 'Mazda RX4 Wag', 'Ford Pantera L' and 'Honda Civic' have.

# In[11]:


# Display cylinders and gear for specific car models
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
# Filter the cars DataFrame to extract only the rows for the models specified in the models list
selected_cars = cars[cars['Model'].isin(models)][['Model', 'cyl', 'gear']]
# To print the selected cars together with the specified rows
print("Cylinders and Gear for selected models:")
selected_cars


# In[ ]:




