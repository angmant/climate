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
import datapackage

#csv files

df = pd.read_csv(r"C:\Users\amanta\Documents\ClimateChange\co2_mm_mlo.csv")


#data convert
df['Date'] = pd.to_datetime(df['Date'])

df['Date'].dt.year

df['Date'].dt.month
 

df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month


df1 = df[['year','month','Trend']]

#keep the beging year and exclude errors = -99.99
dfCo2 = df1[(df1['year'] >= 1900) & (df1['Trend'] >0)]


#groupby selected and mean all the rest

dfCo2group = dfCo2.groupby(['year','month']).mean()

dfCo2group.reset_index(inplace=True)


sns.set_theme()

x = dfCo2group['year']
y = dfCo2group["Trend"]
hue = dfCo2group['month']


# Plot sepal width as a function of sepal_length across days
dfCo2group = sns.lmplot(
    data=dfCo2group,
    x="year", y="Trend", hue="month",
    height=5
)
#Use more informative axis labels than are provided by default
dfCo2group.set_axis_labels("Year", "Ang Treng rate")

plt.show()

np.save("Co2mloFractionSe.npy", [x, y, hue])




