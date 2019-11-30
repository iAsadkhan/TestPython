#!/usr/bin/env python
# coding: utf-8

# In[4]:


a="Why So Serious??"
print(a)


# In[5]:


a='Why '
b='So '
c='Serious??'
print(a+b+c)


# In[6]:


a='Why So Serious??'
print(len(a))


# In[7]:


a="Why So Serious??"
dir(a)


# In[13]:


a='why '
b='so '
c='serious??'
print(a.capitalize()+b.capitalize()+c.capitalize())


# In[16]:


a='Why '
b='So '
c='Serious??'
print(a.casefold()+b.casefold()+c.casefold())


# In[24]:


a="Why So Serious??"
print(a.count('o'))


# In[25]:


a="Why So Serious??"
print(a.upper())


# In[26]:


a="Why So Serious??"
print(a.lower())


# In[27]:


a="why so serious??"
print(a.title())


# In[28]:


a="why so serious??"
print(a.strip())


# In[29]:


a="why so serious??"
print(a.find("serious"))


# In[30]:


a="why so serious??"
print(a.replace('o','i'))


# In[32]:


a="why so serious??"
print(len(a))
print(a.lstrip())
print(len(a.lstrip()))
print(a)


# In[33]:


a="why so serious??"
print(len(a))
print(a.rstrip())
print(len(a.rstrip()))
print(a)


# In[34]:


a="why        so         serious??"
print(len(a))
print(a.strip())
print(len(a.strip()))
print(a)


# In[35]:


a="Why So Serious??"
b=a.split()
b


# In[38]:


a='Why', 'So', 'Serious??'
" ".join(a)


# In[39]:


a="why so serious??"
print(a.endswith('o'))


# In[40]:


a="why so serious??"
print(a.endswith('?'))


# In[48]:


a="""
Why So Serious??
Is an Iconic line by Heath Ledger
In the Movie "The Dark Knight"
"""
print(a)


# In[45]:


Movie= "The Dark Knight"
Line= "Why So Serious??"
Actor= "Heath Ledger"

a="""
Movie= %s
Line= %s
Actor= %s
"""
print(a%(Movie,Line,Actor))


# In[46]:


a="why so serious??"
print(a.expandtabs())


# In[52]:


a="why so serious??"
a.index('so')


# In[53]:


a="why so serious??"
print(a.swapcase())


# In[54]:


a="why so serious??"
print(a.startswith("w"))


# In[ ]:




