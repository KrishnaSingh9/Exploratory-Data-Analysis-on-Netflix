#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Data analysis:- It is process of cleaning, transforming and manipulating the data to finding some insights from out of it
# that might be help to understand the data and make the better decision 


# In[2]:


#Tasks


# In[3]:


# Understand the Dataset, types, and missing values
# Clean the Data and handles the missing values
# Perform Data Visualization
# Create Final report


# In[4]:


#importing libraries
import numpy as np #helps in working arrays and matrices
import pandas as pd #helps in reading datasets/making dataframe/manipulation
import seaborn as sns #visualization
import matplotlib.pyplot as plt #visualization


# In[5]:


#reading the dataset
df=pd.read_csv('C:\\Users\\Admin\\Desktop\\Python\\Netflix\\netflix_titles.csv')
df.head()


# In[6]:


df.shape #row and column


# In[7]:


df.describe() #basic statics for integer column


# In[9]:


df.info() #counts and data types of our columns


# In[11]:


#missing values
df.isna().sum()


# In[ ]:


#adjust data types and fill in missing values
#Check the data types, update types where needed and proceed.(Missing values Columns)


# In[12]:


#convert the data type from object to datetime64
df['date_added']=pd.to_datetime(df['date_added'])


# In[13]:


df.head()


# In[14]:


#Handling missing values
df.fillna({'rating':'Unavailable','cast':'Unavailable','country':'Unavailable','director':'Unavailable'},inplace=True)
df.isna().sum()


# In[ ]:


# For nulls in date_added, missing date_added is to be substituted in with the most recent date from date_added. This is because Netflix
# has the tendency to add more content over time. Other options would be finding actual dates and inputting them manually or dropping
# the data from results since the amount of missing data is rather small.


# In[15]:


df[df.date_added.isnull()]


# In[16]:


most_recent_entry_date=df['date_added'].max()
df.fillna({'date_added':most_recent_entry_date},inplace=True)


# In[ ]:


#Proof that null value has fill with recent date


# In[17]:


df[df.show_id=='s6067']


# In[18]:


df[df.duration.isnull()]


# In[ ]:


#missing value only for Louis C.K


# In[20]:


df[df.director=='Louis C.K.'].head()


# In[ ]:


#overwrite and check


# In[21]:


#loc helps us easily accessing the columns by names
df.loc[df['director']=='Louis C.K.','duration']=df['rating']
df[df.director=='Louis C.K.'].head()


# In[23]:


#second overwrite and check
df.loc[df['director']=='Louis C.K.','rating']='Unaviable'
df[df.director=='Louis C.K.'].head()


# In[ ]:


#Visualizatio


# In[ ]:


#Lets take a look at types of shows that has been watched on Netflix


# In[24]:


df.type.value_counts() #value_counts methods shows us the counts of differenct categories in a given column


# In[25]:


sns.countplot(x='type',data=df) #countplot helps us to plot counts of each category
plt.title('Count Vs Type of Showns')


# In[ ]:


#Country Analysis


# In[27]:


df['country'].value_counts().head(10)


# In[28]:


plt.figure(figsize=(12,6))
sns.countplot(y='country',order=df['country'].value_counts().index[0:10],data=df)
plt.title('Country wise content on Netflix')


# In[29]:


#now checking type of content based on country
movie_countries=df[df['type']=='Movie']
tv_show_countries=df[df['type']=='TV Show']


# In[30]:


plt.figure(figsize=(12,6))
sns.countplot(y='country',order=df['country'].value_counts().index[0:10],data=movie_countries)
plt.title('Top 10 Countries producing movies in Netflix')


plt.figure(figsize=(12,6))
sns.countplot(y='country',order=df['country'].value_counts().index[0:10],data=tv_show_countries)
plt.title('Top 10 Countries producing TV shows in Netflix')


# In[ ]:


#lets check what are the major ratings given to netflix shows


# In[31]:


df.rating.value_counts()


# In[33]:


plt.figure(figsize=(12,6))
sns.countplot(x='rating',order=df['rating'].value_counts().index[0:10],data=df)
plt.title('Rating of shows on Netflix Vs Counts')


# In[ ]:


#most of the shows has TV-MA and TV-14


# In[34]:


df.release_year.value_counts()[0:20]


# In[36]:


plt.figure(figsize=(12,6))
sns.countplot(x='release_year',order=df['release_year'].value_counts().index[0:20],data=df)
plt.title('Content release in years on Netflix Vs Counts')


# In[ ]:


#popular genres analysis


# In[37]:


plt.figure(figsize=(12,6))
sns.countplot(y='listed_in',order=df['listed_in'].value_counts().index[0:20],data=df)
plt.title('Top 20 Genres on Netflix')


# In[ ]:


# Summary
# So, far we had perform lot of operations over the dataset yo dig out some very useful information from it. If we have to
# conclude the dataset in few line then we can say that:
# .Netflix has more movies than TV shows
# .Most number of movies and TV shows produced by US, followed y India who has produced the 2nd most no of movies on netflix.
# .Most of the content on netflix is for mature audiences
# .2018 is the year which netflix released alot of content compared to other years
# .Inernational movies and drams are most polular Genres on netflix.


# In[ ]:





# In[ ]:




