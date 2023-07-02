#!/usr/bin/env python
# coding: utf-8

# In[79]:


class car:
    
    def __init__(self,name,model,cname,speed):
        
        self.__name = name
        self.__model = model 
        self.__cname = cname
        self.__speed = speed
        
    def set_name(self,name):
        self.__name = name if type(name==str) or type(name==int) else False
    
    def get_name(self):
         return self.__name


# In[80]:


o = car('fortuner','huyndia','faraz',20)


# In[81]:


o.set_name('ferari1')


# In[82]:


o.get_name()


# In[66]:


class car :
    def __init__(self , year , make , model, speed ) : 
        
        self.__year = year 
        self.__make = make
        self.__model = model
        self.__speed = speed
        
    def set_speed(self,speed) : 
        self.__speed 
        
    def get_speed(self)  : 
        return self.__speed


# In[67]:


c = car(2021 , "toyata" , "innova" , 12)


# In[69]:


c.get_speed()


# In[56]:


class fa:
    name = 'faraz'
    cl = None


# In[61]:


o = fa()


# In[62]:


o.name


# In[63]:


o.namec= "ali "
o.cl = "yes"


# In[64]:


o.cl


# In[65]:


o.name


# In[ ]:




