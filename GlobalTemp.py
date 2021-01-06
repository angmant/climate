#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('nbagg')
import matplotlib.dates as mdates
#import seaborn as sns
import datetime as dt


# In[2]:


#csv files
#df = pd.read_csv(r"C:\GlobalLandTemperaturesByCountry.csv")
df = pd.read_csv(r"C:\GlobalLandTemperaturesByMajorCity.csv")
#df = pd.read_csv(r"C:\Users\amanta\Documents\ClimateChange\majorTest1.csv")

#data types(object,number,etc)
df.dtypes


# In[3]:


#data convert
df['dt'] = pd.to_datetime(df['dt'])
type(df)
df.dtypes


# In[4]:


df['dt'].dt.year


# In[5]:


type(df)
df.dtypes


# In[6]:


df['dt'].dt.month


# In[7]:


df['year'] = df['dt'].dt.year
df['month'] = df['dt'].dt.month
# if(df['year']==2013):
df.head(21)


#class_23 = titanic[(titanic["Pclass"] == 2) 


# In[8]:


#df['month'] = df['month'].replace([9,10,11],'Autumn')
#df['month'] = df['month'].replace([12,1,2],'Winter')
#df['month'] = df['month'].replace([3,4,5],'Spring')
#df['month'] = df['month'].replace([6,7,8],'Summer')

df1 = df[['year','month','AverageTemperature','AverageTemperatureUncertainty','Country','City']]

#df1.head(21)




# In[9]:


#groupby selected and mean all the rest

# df1.groupby(['year','month','Country','City']).mean()


# In[10]:


#is in
#??δουλεύει αλλά χαλάει το γκρουπάρισμα
#df2 = (df1[df1.month.isin(['Winter', 'Spring'])]
       
# df2 = df1[df1.Country.isin(['UK'])]
# #df2

df2 = df1[df1.Country.isin(['United States','China','Japan','Germany','United Kingdom','India','France','Italy',
                            'Canada','South Korea','Russia','Brazil','Australia','Spain','Indonesia','Mexico','Netherlands',
                            'Switzerland','Saudi Arabia','Turkey','UK'])]
#df2
#does not exist Netherlands and Switzerland
#df2.Country.unique()



#df3 = df2[df1.month.isin(['Winter', 'Spring'])]
#df3
#dfw = df2[df1.month.isin(['Winter'])]

#dfGlobal = df2[df1.year.isin(['Spring'])]

dfGlobal = df2[(df2['year'] >= 1900) & (df2['year'] <= 2015)]
#print(dfGlobal)
#exit()

#check_for_nan = dfGlobal['AverageTemperature'].isnull().values.any()

#check_for_nan=dfGlobal.groupby('year').agg([np.mean,np.std])
#check_for_nan=dfGlobal.describe()

#print(check_for_nan)
#exit()


# In[11]:


# ξανακάνω γκρουπ -> δεν ξέρω εάν γίνεται να ενοθούν δηλ το group by + is in
# πάνω σε αυτό θα βγλάω και τις πόλεις και μετά θα γίνει το πλοτ
#df4 = df3.groupby(['year','month','Country','City']).mean()
#dfGlobalgroup = dfGlobal.groupby(['year','month','Country']).mean()

dfGlobalgroup = dfGlobal.groupby(['year']).mean()


#dfsgroup = dfs.groupby(['year','month','Country','City']).mean()
dfGlobalgroup.reset_index(inplace=True)




#print(dfGlobalgroup)
#exit()

# In[12]:

x = dfGlobalgroup['year']
y = dfGlobalgroup["AverageTemperature"]
DeltaT = []
for Ti in y:
    #print (Ti)
    dT = Ti - y[0]
    DeltaT.append(dT)



#yw = df3.loc[df3['month'] == 'Winter']
#yerr = df3["AverageTemperatureUncertainty"]

plt.xticks(rotation=90)
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.subplots_adjust(bottom=0.22)

#plt.errorbar(dfwgroup["year"], dfwgroup["AverageTemperature"], yerr=None, fmt='o' )
plt.errorbar(x, y, yerr=None, fmt='o' )


fig1, ax1 = plt.subplots()


ax1.errorbar(x, DeltaT, yerr=None, fmt='o', markersize=0.5)



plt.show()




np.save("GlobalYear.npy", [x, y])



