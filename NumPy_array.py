#!/usr/bin/env python
# coding: utf-8

# In[2]:


my_list = [1,2,3]
import numpy as np
arr = np.array(my_list)
arr


# In[3]:


my_mat = [[1,2,3],[4,5,6],[7,8,9]]
np.array(my_mat)


# In[4]:


np.arange(0,10)


# In[6]:


np.arange(0,11,2)


# In[7]:


np.zeros(3)


# In[9]:


np.zeros((2,3))


# In[10]:


np.ones((3,4))


# In[12]:


np.linspace(0,5,100)


# In[13]:


"""identiy matrix"""
np.eye(4)


# In[14]:


np.random.rand(5)


# In[15]:


np.random.rand(5,5)


# In[17]:


"""sample from gausian distribution/normal distribution"""
np.random.randn(4,4)


# In[18]:


np.random.randint(1,100)


# In[20]:


arr = np.arange(25)
ranarr = np.random.randint(0,50,10)
ranarr


# In[21]:


arr.reshape(5,5)


# In[22]:


ranarr


# In[23]:


ranarr.max() #find the  max element 


# In[25]:


ranarr.min() #find the  min element


# In[26]:


ranarr.argmin() #index of max element


# In[27]:


ranarr.argmax() #index of min element


# In[28]:


arr = arr.reshape(5,5)

arr


# In[29]:


arr.shape #check the shape


# In[30]:


arr.dtype #check the datatype


# In[ ]:




