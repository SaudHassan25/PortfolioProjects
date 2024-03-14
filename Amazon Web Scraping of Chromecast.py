#!/usr/bin/env python
# coding: utf-8

# In[48]:


from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
import pandas as pd


# In[71]:


URL = "https://www.amazon.com/Google-Chromecast-TV-HD-NO/dp/B0BGCDL1S3/ref=sr_1_8?dib=eyJ2IjoiMSJ9.c1NF21M2LNd2yCGdDR9F8n5lsDGi1IrBXD6kFgYA8LsI4H_MY3sPTGUfDxkrpmqnbRSfz0vfVQUsPsVKN2Jb9htzYlhmXu-1fKZ7ej6lX3x87O5nLKP7DbQ5sUUC47SV1-fI3TlG1YlELKEGhJyahOxYHWYoaL4KQ2hUoCU3RrRq3u9CENVKc-_ufzATxdPBuZDfuQ-z1gBOmmcVz_KaJorFehHsDLufph6N3d6tmGg.37fxmcBbtHbTx_unP2cThoCtw6b9sQF57BiGCn0F92s&dib_tag=se&keywords=chrome+cast&qid=1710150215&sr=8-8"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content,'html.parser')

soup2 = BeautifulSoup(soup1.prettify(),'html.parser')

title = soup2.find(id = 'productTitle').get_text()
price = soup2.find("span",{"class":"a-price"}).find("span").text

print(title)
print(price)


# In[80]:


title = title.strip()
price = price.strip()[1:]

print(title)
print(price)


# In[61]:


today = datetime.date.today()

print(today)


# In[63]:


import csv
header = ['Title','Price','Date']
data = [title,price]


with open('AmazonWebScraping.csv','w',newline = '',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[70]:


df = pd.read_csv(r"C:\Users\MM COMPUTERS/AmazonWebScraping.csv")
print(df)


# In[73]:


with open('AmazonWebScraping.csv','a+',newline = '',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[78]:


while(True):
    check_price()
    time.sleep(86400)


# In[77]:


def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?customId=B0752XJYNL&dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content,'html.parser')

    soup2 = BeautifulSoup(soup1.prettify(),'html.parser')

    title = soup2.find(id = 'productTitle').get_text()
    price = soup2.find("span",{"class":"a-price"}).find("span").text

    title = title.strip()
    price = rating.strip()
    
    today = datetime.date.today()
    
    import csv
    
    header = ['Title','Price','Date']
    data = [title,rating,today]
    
    with open('AmazonWebScraping.csv','a+',newline = '',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




