#!/usr/bin/env python
# coding: utf-8

# In[1]:


class faraz:
    
    def __init__(self,name,emailid):
        
        self.name = name 
        self.emailid =  emailid
        
    def student_details(self):
        print(self.name,self.emailid)
        
    


# In[4]:


obj = faraz('faraz ali khan', 'ff@gmail.com')


# In[5]:


obj.emailid


# In[7]:


obj.student_details()


# In[9]:


faraz.mro()


# In[26]:


class faraz1:
    
    def __init__(self,name,emailid):
        
        self.name = name 
        self.emailid =  emailid
        
    @classmethod
    def details(cls,name,emailid):
        return cls(name,emailid)
        
    def student_details(self):
        print(self.name,self.emailid)
    
    
        
    


# In[27]:


## HERE I AM WITHOUT CREATING OBJECT I AM PASSING THE DATA TO THE CLASS


# In[28]:


faraz1.details('faraz' , "kk@gmial.com")


# In[38]:


f = faraz1.details('faraz' , "kk@gmial.com")


# In[30]:


f.name


# In[32]:


f.emailid


# In[40]:


f.student_details()


# In[46]:


class faraz2:
    
    # IT IS AN CLASS VARIABLE
    
    mobile_num = 7411046755
    
    
    def __init__(self,name,emailid):
        
        self.name = name 
        self.emailid =  emailid
        
    @classmethod
    def change_num(self,num):
        faraz2.mobile_num = num
        
        
    @classmethod
    def details(cls,name,emailid):
        return cls(name,emailid)
        
    def student_details(self):
        print(self.name,self.emailid)
    
    
        
    


# In[47]:


faraz2.mobile_num


# In[49]:


faraz2.change_num(9964763232)


# In[55]:


faraz2.mobile_num


# In[ ]:


class faraz3:
    
    def __init__(self,name,emailid):
        
        self.name = name 
        self.emailid =  emailid
        
    @classmethod
    def details(cls,name,emailid):
        return cls(name,emailid)

    
    @classmethod
    def set_name(self,name):
        faraz3.name = name
    
    def student_details(self):
        print(self.name,self.emailid)
        
        
    


# In[57]:


g = faraz3.details('faraz','kkkk@.com')


# In[58]:


g.name


# In[59]:


g.set_name('tabrez')


# In[60]:


faraz3.name


# In[61]:


g.name


# In[62]:


faraz3.set_name('ali')


# In[63]:


faraz3.name


# In[ ]:





# In[65]:


class faraz3:
    
    def __init__(self,name,emailid):
        
        self.name = name 
        self.emailid =  emailid
        
    @classmethod
    def details(cls,name,emailid):
        return cls(name,emailid)

    
    @classmethod
    def set_name(self,name):
        faraz3.name = name
    
    def student_details(self):
        print(self.name,self.emailid)
        
        
    


# ## ADDING OUTSIDER FUNCTION INSIDE THE CLASS 

# In[67]:


def course_details(cls,course_name):
    print("course name is :" ,course_name)


# In[68]:


faraz3.course_details = classmethod(course_details)


# In[69]:


faraz3.course_details('daata science')


# In[70]:


def mentor(cls,list_of_mentor):
    print(list_of_mentor)


# In[73]:


faraz3.mentor = classmethod(mentor)


# In[74]:


faraz3.mentor(['faraz','tabrez' , 'arbaz'])


# ## DELETING THE CLASS METHODS AND VARIABLES FROM THE CLASS 

# In[75]:


del faraz3.course_details


# In[76]:


## ANOTHER METHOD OF DELETING
delattr(faraz3,'mentor')


# In[ ]:





# In[ ]:




