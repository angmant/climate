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

#getting discription 
#desc = dfGl.describe()
#dfDescr.reset_index(inplace=True)   

#Number of observations

#Creating the plot

x = dfGl['Year']
y = dfGl["Mean cumulative mass balance"]
#err = dfGroup["std"]



plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.22)
plt.title(' Mean cumulative mass balance by Year')
plt.xlabel('Year')
plt.ylabel(' Mean cumulative mass balance')
plt.grid(b=True, which='major', color='#666666', linestyle='-')

plt.errorbar(x, y, yerr=None, fmt='o', ecolor='lightblue', elinewidth=0.5, capsize=0, markersize=2)


sns.set_theme(style="darkgrid")

g = sns.jointplot(x="Year", y="Gleciers mean cumulative mass balance", data=dfGl,
                  kind="reg", truncate=False,
                  #xlim=(0, 60), ylim=(0, 12),
                  color="m", height=8)


plt.show()
#--------


np.save("Glaciers.npy", [x, y])



