#!/usr/bin/env python
# coding: utf-8

# ## **MAVEN AIRLINE EXPLORATORY ANALYSIS**
# 
# ---
# 
# 
# 
# 

# 

# 

# 

# In[6]:


#importig all necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


#uploding file

#from google.colab import files
#uploaded = files.upload()


# In[ ]:


#import io 
#df = pd.read_excel(io.BytesIO(uploaded['airline_passenger_satisfaction.xlsx']))
#df.head()


# In[8]:


df = pd.read_excel(r"C:\Users\Daisy\Desktop\airline_passenger_satisfaction.xlsx")
df.head()


# In[9]:


df.shape


# In[10]:


df.describe()


# In[11]:


df.isna().sum()


# In[12]:


airline = df.fillna(0)


# In[13]:


airline.isna().sum()


# In[14]:


airline.info()


# In[15]:


def count(rows):
          return len(rows)
a = airline.groupby('Gender').apply(count)
print(a)


# In[16]:


ax = sns.boxplot(x = 'Age', y = 'Class', data = airline)
ax.set_title('Age Vs class')
ax.set_xlabel('Age')
ax.set_ylabel('Class')


# In[17]:


plt.figure(figsize = (8,6))
sns.countplot(airline['Class'])


# In[18]:


plt.figure(figsize = (8,6))
sns.countplot(airline['Satisfaction'])


# In[19]:


plt.figure(figsize = (20,10))
c= airline.corr()
sns.heatmap(c,cmap='BrBG',annot=True)


# In[20]:


airline.columns


# In[21]:


columns = ['ID', 'Gender', 'Age', 'Customer Type', 'Type of Travel', 'Class',
       'Flight Distance', 'Departure Delay', 'Arrival Delay',
       'Departure and Arrival Time Convenience', 'Ease of Online Booking',
       'Check-in Service', 'Online Boarding', 'Gate Location',
       'On-board Service', 'Seat Comfort', 'Leg Room Service', 'Cleanliness',
       'Food and Drink', 'In-flight Service', 'In-flight Wifi Service',
       'In-flight Entertainment', 'Baggage Handling', 'Satisfaction']
       


# In[ ]:


for col in columns:
  fig = plt.figure(figsize = (9,6))
  ax = fig.gca()
  feature = airline[col].value_counts()
  feature.plot.bar(ax=ax)
  ax.axvline(feature.mean(),color = 'yellow', linestyle = 'dashed', linewidth = 2)
  ax.set_title(col)
  plt.show()


# In[ ]:


fig, ax = plt.subplots(nrows = 5, ncols = 5)
for ax in ax:
    ax.plt(airline, 'r')


# In[ ]:


sns.pairplot(airline, hue='Gender')


# In[ ]:


2+2


# In[ ]:




