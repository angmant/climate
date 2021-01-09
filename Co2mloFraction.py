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
import statistics


# In[2]:


#csv files from https://datahub.io/core/co2-ppm

df = pd.read_csv(r"C:\Users\amanta\Documents\ClimateChange\co2_mm_mlo.csv")

#print(df)
#exit()


#data convert
df['Date'] = pd.to_datetime(df['Date'])

df['Date'].dt.year

df['Date'].dt.month
 

df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month


df1 = df[['year','month','Trend']]

dfCo2 = df1[(df1['year'] >= 1900) & (df1['Trend'] >0)]


#groupby selected and mean all the rest
#dfCo2group = dfCo2.groupby(['year','month']).mean()

#described_dfCo2group = dfCo2group['Average'].describe()

dfGroup = dfCo2.groupby('year').agg(
    {'month':['count'],
        'Trend':['mean', 'std']})


#dfCo2group = dfCo2.groupby('year','Status').mean()
      
dfGroup.columns = dfGroup.columns.droplevel(0) 

dfGroup.reset_index(inplace=True)

#Creating plt

x = dfGroup['year']

y = dfGroup["mean"]

err = dfGroup["std"]

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.95)

# Set titles for the figure and the subplot respectively
fig.suptitle('', fontsize=14, fontweight='bold')
ax.set_title('Growth rate of Carbon Dioxide')

ax.set_xlabel('Year')
ax.set_ylabel('Trends CO2 mole fraction')

plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.22)

plt.errorbar(x, y, yerr=err, fmt='o' )
plt.grid()
plt.show()


np.save("Co2mloFraction.npy", [x, y, err])


# In[ ]:





# In[ ]:




