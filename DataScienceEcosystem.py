#!/usr/bin/env python
# coding: utf-8

# # Data Science Tools and Ecosystem

# In this notebook, Data Science Tools and Ecosystem are sumarized.

# - General knowledge
#     - Data Science Languages
#     - Data Science Libraries
# - Example of arithmetic expression
# - Author
# 

# Some of the popular languages that Data Scientists use are:
# ordered list:
# Python, R, SQL, Julia, Scala, Java

# Some of the commonly used libraries used by Data Scientists include:
# 1. Numpy
# 2. Pandas
# 3. Matplotlib
# 4. Seaborn
# 5. Scikit-learn
# 6. Tensor Flow
# 7. PyTorch

# |Data Science Tools|
# |------------------|
# |Jupiter Notebook  |
# |RStudio           |
# |Spider            |
# 

# ### Below are a few examples of evaluating arithmetic expressions in Python

# In[12]:


# This a simple arithmetic expression to mutiply then add integers
(3*4)+5


# In[11]:


# This will convert two houndred minutes to hours by diving by sixty
def convert_minutes_to_hours(minutes):
    hours = minutes / 60
    return hours

# Example: Convert 200 minutes to hours
minutes = 200
hours_result = convert_minutes_to_hours(minutes)

# Display the result
print(f"{minutes} minutes is equal to {hours_result:.2f} hours")


# ## Author: Miguel Castillo
