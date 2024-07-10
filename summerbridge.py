#!/usr/bin/env python
# coding: utf-8

# In[ ]:


3 + 7


# In[ ]:


print("hello")


# In[ ]:


print(7)


# In[ ]:


name = "Derek"
age = 42


# In[ ]:


print(age)


# In[ ]:


# This is a comment. It will not run 
# You can echo values without using print in this notebook
name


# # Variables and values

# In[ ]:


# Variables can be used in calculations
print(age)
age = age + 3
print(age)


# In[ ]:


# Order of operations matters!
first = 1
second = first*5
first = 2
print(first)
print(second)


# In[ ]:


# Values have types. Types affect what you can do with them. 
print(5-3)
#print("hello" - "h")


# In[ ]:


print(len("hello"))
#print(len(6))


# ## Challenge 
# Explain what each operator does 
# 
# print(5 // 3)
# 
# print(5 / 3)
# 
# print(5 % 3)

# In[ ]:


print(5//3)
print(5/3)
print(5%3)


# # Getting help

# In[ ]:


# Rounding numbers is built in
round(3.14159)


# In[ ]:


round(3.14159, 2)


# In[ ]:


help(round)


# In[ ]:


round(3.14159, ndigits = 2)


# In[ ]:


# All functions return a new value
rounded_pi = round(3.14159, 2)
print(rounded_pi)


# ## Challenge
# 
# In what order do the operations happen?
# 
# radiance = 1.0
# 
# radiance = max(2.1, 2.0 + min(radiance, 1.1 * radiance - 0.5))

# In[ ]:


radiance = 1.0
print(radiance*1.1-0.5)
radiance = max(2.1, 2.0 + min(radiance, 1.1 * radiance - 0.5))
print(radiance)


# In[ ]:


help(min)


# In[ ]:


# Break down these operations
radiance = 1.0 

min_arg_2 = 1.1 * radiance - 0.5
print("Min arg 2:", min_arg_2)

min_result = min(radiance, min_arg_2)
print("Min result:", min_result)

radiance = max(2.1, 2.0 + min_result)
print(radiance)


# # A Brief Interlude with Git

# In[ ]:





# In[ ]:




