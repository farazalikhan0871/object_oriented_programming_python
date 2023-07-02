#!/usr/bin/env python
# coding: utf-8

# ## POLYMORPHISM
# 

# In[4]:


class data_science():
    
    def syllabus(self):
        print("this is the syllabus for data science")


# In[5]:


class machine_learning():
    
    def syllabus(self):
        print("this is the syllabus for machine learing")


# In[6]:


ob1 = data_science()


# In[7]:


ob2 = machine_learning()


# In[8]:


myfun= [ob1,ob2]


# In[19]:


def fun1(myfun):
    for i in myfun:
        i.syllabus()


# In[20]:


fun1(myfun)


# In[ ]:




