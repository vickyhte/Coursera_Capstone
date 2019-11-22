#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd


# #### 1 - Scrape the table from Wikipedia page

# In[ ]:


df = pd.read_html('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')[0]


# #### 2 - Only process the cells that have an assigned borough. Ignore cells with a borough that is Not assigned

# In[26]:


df = df[df.Borough != 'Not assigned']


# #### 3 - More than one neighborhood can exist in one postal code area. The rows will be combined into one row with the neighborhoods separated with a comma.

# In[27]:


df = df.groupby('Postcode').agg(lambda x:','.join(set(x)))


# #### 4 - The neighborhood will be the same as the borough, if a cell has a borough but a Not assigned neighborhood.

# In[ ]:


df.loc[df['Neighbourhood'] == 'Not assigned' , 'Neighbourhood'] = df.loc[df['Neighbourhood'] == 'Not assigned' , 'Borough']


# #### 5 -  Print the number of rows

# In[30]:


df.shape


# ### A glance at the result

# In[33]:


df


# In[ ]:




