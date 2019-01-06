#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
arr = np.arange(1,11)
arr


# In[2]:


arr[8]


# In[4]:


arr[1:5]


# In[5]:


arr[0:5]


# In[6]:


arr[5:]


# In[7]:


arr[:5]


# In[8]:


arr[0:5] = 100


# In[9]:


arr


# In[11]:


arr


# In[13]:


slice_of_arr = arr[0:6]
slice_of_arr


# In[14]:


slice_of_arr[:] = 99


# In[15]:


arr


# In[17]:


arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
arr_2d


# In[18]:


arr_2d[0][1] #grabing element in first row in first column


# In[19]:


arr_2d[1][1] #this is called double bracket notation


# In[21]:


arr_2d[1,1] #this is a single bracket noation


# In[22]:


arr_2d[:2,1:]


# In[27]:


bool_arr = arr > 5
bool_arr


# In[26]:


arr[bool_arr]


# In[28]:


arr_2d = np.arange(50).reshape(5,10)


# In[31]:


arr_2d[1:3,3:5]


# In[ ]:




