#!/usr/bin/env python
# coding: utf-8

# In[8]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'e92dee9e-c777-425d-8c03-a441cb9d92fe',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

#NOTE:
# I had to go in and put "jupyter notebook --NotebookApp.iopub_data_rate_limit=1e10"
# Into the Anaconda Prompt to change this to allow to pull data


# In[56]:


import pandas as pd

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


# In[9]:


#This normalizes the data and makes it all pretty in a dataframe

df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('now')
df


# In[140]:


def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'15',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'e92dee9e-c777-425d-8c03-a441cb9d92fe',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    
    df2 = pd.json_normalize(data['data'])
    df2['timestamp'] = pd.to_datetime('now')
    df_append = pd.DataFrame(df2)
    df = pd.concat([df,df_append])
    #Once we ran it we should not run it again,if we want the data into csv,otherwise it will make copies of data.So, we have
    #to run the below function to prevent it.
    
    
    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')
    df
    
    if not os.path.isfile(r'E:\API\File.csv'):
        df.to_csv(r'E:\API\File.csv', header = 'column names')
    else:
        df.to_csv(r'E:\API\File.csv',mode = 'a' ,header = False)


# In[141]:


import os
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print('API Runner Completed')
    sleep(60)
exit()



# In[139]:


df


# In[142]:


df3 = pd.read_csv(r'E:\API\File.csv')
df3


# In[143]:


# One thing I noticed was the scientific notation. I like it, but I want to be able to see the numbers in this case


pd.set_option('display.float',lambda x: '%.5f' %x)


# In[144]:


df


# In[145]:


df4 = df.groupby('name',sort = False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
df4


# In[146]:


df5 = df4.stack()
df5


# In[147]:


type(df5)


# In[148]:


df6.count()


# In[149]:


df6 = df5.to_frame(name = 'values')
df6


# In[150]:


index = pd.Index(range(90))


# In[151]:


df7 = df6.reset_index()
df7


# In[152]:


df8 = df7.rename(columns={'level_1':'percent_change'})
df8


# In[153]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[154]:


df8['percent_change'] = df8['percent_change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['1H','24H','7D','30D','60D','90D'])
df8


# In[155]:


sns.catplot(x = 'percent_change', y = 'values', hue = 'name', data = df8, kind = 'point')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




