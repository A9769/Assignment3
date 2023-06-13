#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import os
import matplotlib.pyplot as plt


# In[2]:


air = pd.read_csv("Airbnb Dataset 19_1.csv")


# In[3]:


hr = pd.read_csv("HRDataset_v14_1.csv")


# In[4]:


air.head()


# In[7]:


hr.head()


# In[8]:


air.isnull().sum()


# In[9]:


hr.isnull().sum()


# In[5]:


air.head()


# In[6]:


air.duplicated().sum()
air.drop_duplicates(inplace=True)


# In[7]:


air.describe()


# In[8]:


air.drop(['id','name','host_name','last_review'], axis=1, inplace=True)


# In[9]:


air.head(5)


# In[10]:


air.columns


# In[11]:


corr= air.corr(method='kendall')
plt.figure(figsize=(10,6))
sns.heatmap(corr,annot=True)
air.columns


# In[ ]:


### in this visualization we see correlatin between different variable available on each columns


# In[12]:


air['neighbourhood_group'].unique()


# In[13]:


air.neighbourhood_group = air.neighbourhood_group.astype('category') 


# In[14]:


air.neighbourhood_group.cat.categories


# In[17]:


pd.crosstab(air.neighbourhood_group, air.room_type)


# In[15]:


sns.catplot(x='room_type', y='price', data=air);


# In[ ]:


### As per above visualization we shown how price is plotting among three difference rooms.


# In[16]:


plt.figure(figsize=(10,10))
air1 = sns.countplot(x=air['room_type'], hue=air['neighbourhood_group'], 
                     palette='plasma')


# In[ ]:


## in above Visualization we create countplot of Roomtype & neighbourhood group


# In[17]:


plt.figure(figsize=(8,8))
air1 = sns.boxplot(data=air, x="neighbourhood_group",y="availability_365", palette="plasma")


# In[ ]:


## in above visualization we create boxplot in neighbourhood group & room availablity 365


# In[18]:


plt.style.use('fivethirtyeight')
plt.figure(figsize=(13,7))
plt.title("Neighbourhood Group")
g= plt.pie(air.neighbourhood_group.value_counts(), labels=air.neighbourhood_group.value_counts().
          index,autopct='%1.1f%%', startangle=180)
plt.show()


# In[19]:


hr.head()


# In[20]:


hr.shape


# In[21]:


hr['PerformanceScore'].value_counts()


# In[27]:


plt.subplots(figsize=(13,4))
hr['PerformanceScore'].value_counts(normalize=True)
hr['PerformanceScore'].value_counts(dropna=False).plot.bar(color=
                            ['Green','Blue','Orange','Red'])
plt.show()


# In[28]:


hr['RecruitmentSource'].value_counts()


# In[40]:


size = [87,76,49,31,29,23,13,2,1]
colors = ['Yellow','Blue','Green','Pink','Red','Orange','black','brown','cyan']
labels = "Indeed","LinkedIn","Google Search","Employee Referral","Diversity Job Fair","CareerBuilder","Website","Other","On-line web application"

circle= plt.Circle((0,0), 0.7, color = 'white')
plt.rcParams['figure.figsize']= (9,9)
plt.pie(size, colors= colors, labels= labels, shadow=True, autopct= '%.2f%%')
plt.title('showing share of diffrent Recruitment channels', fontsize=24)
p = plt.gcf()
p.gca().add_artist(circle)
plt.legend()
plt.show()


# In[49]:


hr.plot.scatter(x='EmpSatisfaction',y='Absences', c='red', s=50, figsize=(10,5))


# In[50]:


### in this visualization we plotting toghether on Employees absent on with Satisafaction level 


# In[52]:


hr['EngagementSurvey'].plot.kde()


# In[ ]:


### in this visualizaion we showcase how Engaement survey is distributed among employees


# In[62]:


hr.plot(x='EmpSatisfaction', y=['PerfScoreID','Salary'])
plt.show()


# In[ ]:


### in this Visualizaion we showcanse a relation ship between Employee Salary with this perfect score on the basis of EMp Satisfaction

