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


df = pd.read_csv(r"C:\Users\amanta\Documents\ClimateChange\glaciers.csv")


dfGl = df[(df['Year'] > 1945) ]

#   Year  Mean cumulative mass balance  Number of observations

#getting discription 
#desc = dfGl.describe()
#dfDescr.reset_index(inplace=True)   


#Global
df = pd.read_csv(r"C:\Users\amanta\Documents\ClimateChange\GlobalTemperatures.csv")

#data convert
df['dt'] = pd.to_datetime(df['dt'])
df['dt'].dt.year
df['dt'].dt.month
df['year'] = df['dt'].dt.year
df['month'] = df['dt'].dt.month
df1 = df[['year','month','LandAndOceanAverageTemperature']]
dfGlobal = df1[(df1['year'] >= 1945) ]
#getting discription 
dfDescr = dfGlobal.describe()
dfDescr.reset_index(inplace=True)   

#getting the std from average temperature

dfGroup = dfGlobal.groupby('year').agg(
    {'month':['count'],
        'LandAndOceanAverageTemperature':['mean', 'std']})
       
 
#fixing the title row 
dfGroup.columns = dfGroup.columns.droplevel(0) 
dfGroup.reset_index(inplace=True)


#Creating the plot

x = dfGl['Year']
y = dfGl['Mean cumulative mass balance']
#ygerr = npyData[2]
xgl = dfGroup['year']
ygl = dfGroup['mean']

#-------------------

plt.subplot(2, 1, 1)
plt.plot(xgl, ygl, 'o-', markersize=3, linewidth=0.3,color="orange" )
plt.title('Average Global Temperature \n vs \n Average mass of measured glacier', 
          fontsize=14, 
          color="black")
          
plt.ylabel('Avg Temperature') 
plt.grid(b=True, which='major', color='grey', linestyle='-.', linewidth=0.3)

plt.subplot(2, 1, 2)
plt.plot(x, y, '.-',color="orange")
plt.xlabel('Year')
plt.ylabel('Avg mass glacier')
plt.grid(b=True, which='major',color='grey', linestyle='-.', linewidth=0.3)

plt.show()

np.save("GlaciersVsGTemperature.npy", [x, y, xgl, ygl])

exit()



#
#plt.ylim(-30, 20)
plt.yticks(np.arange(-30, 30, 2))

plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.22)
plt.title('Average Global Temperature by Year')
plt.xlabel('Year')
plt.ylabel('mean Global Temperature')
plt.grid(b=True, which='major', color='#666666', linestyle='-')

plt.errorbar(x, y, yerr=None, fmt='o', ecolor='lightblue', elinewidth=0.2, capsize=0)
plt.errorbar(x=xgl, y=ygl, yerr=None, fmt='o', ecolor='lightblue', elinewidth=0.2, capsize=0)

plt.show()




