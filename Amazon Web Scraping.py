#!/usr/bin/env python
# coding: utf-8

# In[206]:


#import libraries

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[217]:


#Connect to Website

URL = 'https://www.amazon.com/Logitech-SUPERLIGHT-Ultra-Lightweight-Programmable-Compatible/dp/B087LXCTFJ/ref=sr_1_2?keywords=superlight+x+logitech&qid=1689416136&sprefix=superlight%2Caps%2C183&sr=8-2'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html")

soup2 = BeautifulSoup(soup1.prettify(), "html")

title = soup2.find(id='title').get_text()

rating = soup2.find(id='acrCustomerReviewText').get_text()

print(title)
print(rating)


# In[218]:


rating = rating.strip()
title = title.strip()

print(title)
print(rating)


# In[219]:


today = datetime.date.today()
print(today)


# In[220]:


import csv

header = ['Title', 'Rating', 'Date']
data = [title, rating, today]

with open('AmazonWebScrapperDataset.csv', 'w', newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[221]:


import pandas as pd


# In[ ]:


df = pd.read_csv(r"C:\Users\David\AmazonWebScrapperDataset.csv")
df


# In[223]:


#Appending data to csv

with open('AmazonWebScrapperDataset.csv', 'a+', newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[224]:


def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html")

    soup2 = BeautifulSoup(soup1.prettify(), "html")

    title = soup2.find(id='productTitle').get_text()

    rating = soup2.find(id='acrCustomerReviewText').get_text()
    
    rating = rating.strip()
    
    title = title.strip()
    
    import datetime
    
    today = datetime.date.today()
    
    import csv

    header = ['Title', 'Rating', 'Date']
    data = [title, rating, today]

    with open('AmazonWebScrapperDataset.csv', 'a+', newline='',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[ ]:


while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




