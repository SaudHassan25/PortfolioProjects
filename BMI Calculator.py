#!/usr/bin/env python
# coding: utf-8

# In[9]:


Name = input("Enter your Name:")
Weight = int(input("Enter your Weight in Pounds:"))
Height = int(input("Enter your Height in Inches:"))


BMI = (Weight *703)/(Height*Height)

print(BMI)

if BMI>0:
    if( BMI<18.5):
        print(Name + ",You are Underweight.")
    elif( BMI<=24.9):
            print(Name + ",You are Balanced.")
    elif( BMI<29.9):
            print(Name + ",You are Overweight.")
    elif( BMI<34.9):
            print(Name + ",You are Obese.")
    elif( BMI<39.9):
            print(Name + ",You are Severly Obese.")
    else:
        print(Name + ",You are Morbidly Obese.")

    


# In[ ]:





# In[ ]:




