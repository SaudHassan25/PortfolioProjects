#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os,shutil


# In[2]:


path = r"D:/python fie sorter/"


# In[3]:


file_name = os.listdir(path)


# In[4]:


folder_names = ['text files','image files','Excel files']

for folder in range(0,3):
    if not os.path.exists(path + folder_names[folder]):
        os.makedirs(path + folder_names[folder])





for file in file_name:
    if ".csv" in file and not os.path.exists(path + "text files/" + file ):
        shutil.move(path + file,path + "text files/" + file)
    if ".png" in file and not os.path.exists(path + "image files/" + file ):
        shutil.move(path + file,path + "image files/" + file)
    if ".jpg" in file and not os.path.exists(path + "image files/" + file ):
        shutil.move(path + file,path + "image files/" + file)
    if ".xlsx" in file and not os.path.exists(path + "Excel files/" + file ):
        shutil.move(path + file,path + "Excel files/" + file)



# In[ ]:




