#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, shutil 


# In[6]:


path = r"C:/Users/David/OneDrive/Desktop/data analyst projects/"


# In[8]:


file_name = os.listdir(path)


# In[12]:


folder_names = ['csv files', 'sql files', 'pbix files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))
        
for file in file_name: 
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file , path + "csv files/" + file)
    elif ".sql" in file and not os.path.exists(path + "sql files/" + file):
        shutil.move(path + file , path + "sql files/" + file)
    elif ".pbix" in file and not os.path.exists(path + "pbix files/" + file):
        shutil.move(path + file , path + "pbix files/" + file)


# In[9]:





# In[ ]:





# In[ ]:




