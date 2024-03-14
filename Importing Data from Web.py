#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[4]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text,'html')


# In[5]:


print(soup)


# In[6]:


soup.find('table')


# In[8]:


soup.find_all('table')[1]


# In[9]:


soup.find('table',class_ = 'wikitable sortable')


# In[10]:


table = soup.find_all('table')[1]


# In[11]:


print(table)


# In[19]:


world_titles = table.find_all('th')


# In[20]:


world_titles


# In[21]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[24]:


import pandas as pd


# In[26]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[28]:


column_data = table.find_all('tr')


# In[32]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[33]:


df


# In[39]:


df.to_csv(r'D:\imported_data.csv', index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




