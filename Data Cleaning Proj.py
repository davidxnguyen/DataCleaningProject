#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[53]:


df = pd.read_excel(r"C:\Users\David\Downloads\Customer Call List.xlsx")
df


# In[54]:


df = df.drop_duplicates()
df


# In[55]:


df = df.drop(columns = 'Not_Useful_Column')
df


# In[56]:


#df['Last_Name'] = df['Last_Name'].str.lstrip("...")
#df['Last_Name'] = df['Last_Name'].str.lstrip("/")
#df['Last_Name'] = df['Last_Name'].str.rstrip("_")
df['Last_Name'] = df['Last_Name'].str.strip("123._/")
df


# In[65]:


#df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]', '')

#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))

#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')

df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')

df


# In[69]:


df[["Street_Address","State","Zip_Code"]] = df['Address'].str.split(',', 2, expand=True)
df


# In[72]:


df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes', 'Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No', 'N')
df


# In[79]:


#df = df.replace('N/a', '')
#df = df.replace('NaN', '')

df = df.fillna('')

df


# In[80]:


for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace = True)

df


# In[81]:


for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace = True)

df


# In[84]:


df = df.reset_index(drop = True)
df


# In[ ]:




