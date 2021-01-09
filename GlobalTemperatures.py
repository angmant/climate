#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('nbagg')
import matplotlib.dates as mdates
import seaborn as sns
import datetime as dt


# In[2]:


#csv files
#df = pd.read_csv(r"C:\GlobalLandTemperaturesByCountry.csv")
#df = pd.read_csv(r"C:\GlobalLandTemperaturesByMajorCity.csv")
df = pd.read_csv(r"C:\Users\amanta\Documents\ClimateChange\GlobalTemperatures.csv")

#data types(object,number,etc)
#df.dtypes


# In[3]:


#data convert
df['dt'] = pd.to_datetime(df['dt'])
#type(df)
#df.dtypes


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


df1 = df[['year','month','LandAndOceanAverageTemperature']]


dfGlobal = df1[(df1['year'] >= 1900) ]

#getting discription 
dfDescr = dfGlobal.describe()
dfDescr.reset_index(inplace=True)   

#Checking for NaN values
check_for_nan = dfGlobal['LandAndOceanAverageTemperature'].isnull().values.any()

#Grouping by year - count the months and mean the Temperature by year
#getting the std from average temperature

dfGroup = dfGlobal.groupby('year').agg(
    {'month':['count'],
        'LandAndOceanAverageTemperature':['mean', 'std']})
       
 
#fixing the title row 
dfGroup.columns = dfGroup.columns.droplevel(0) 

dfGroup.reset_index(inplace=True)

#Creating the plot

x = dfGroup['year']
y = dfGroup["mean"]
err = dfGroup["std"]


DeltaT = []
for Ti in y:
    #print (Ti)
    dT = Ti - y[0]
    DeltaT.append(dT)


plt.xticks(rotation=90)

plt.subplots_adjust(bottom=0.22)
plt.title('Average Global Temperature by Year')
plt.xlabel('Year')
plt.ylabel('mean Global Temperature')
plt.grid(b=True, which='major', color='#666666', linestyle='-')

plt.errorbar(x, y, yerr=err, fmt='o', ecolor='lightblue', elinewidth=0.5, capsize=0)


fig1, ax1 = plt.subplots()
ax1.errorbar(x, DeltaT, yerr=err, fmt='o', markersize=0.5)



fig2, ax2 = plt.subplots()
ax2.hist(y[0:20],bins = 10, label = '{:d}-{:d}'.format(x[0], x[20]), histtype='step', stacked=True, fill=False)

ax2.hist(y[21:40],bins = 10, label = '{:d}-{:d}'.format(x[21], x[40]), histtype='step', stacked=True, fill=False)
ax2.hist(y[41:60],bins = 10, label = '{:d}-{:d}'.format(x[41], x[60]), histtype='step', stacked=True, fill=False)
ax2.hist(y[61:80],bins = 10, label = '{:d}-{:d}'.format(x[61], x[80]), histtype='step', stacked=True, fill=False)
ax2.hist(y[81:100],bins = 10, label = '{:d}-{:d}'.format(x[81], x[100]), histtype='step', stacked=True, fill=False)
#ax2.hist(y[46:60],bins = 20, label = '{:d}-{:d}'.format(x[46], x[60]), histtype='step', stacked=True, fill=False)

ax2.legend( bbox_to_anchor=(0.7, 1),loc='upper left')

plt.show()
exit()


np.save("GlobalTemperatures.npy", [x, y, err, DeltaT])



