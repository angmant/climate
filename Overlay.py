
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('nbagg')
import matplotlib.dates as mdates
#import seaborn as sns
import datetime as dt

npyData = np.load('GlobalTemperatures.npy')
npyDataCo2 = np.load("Co2Fraction.npy")
npyDataSe = np.load("GlobalTemperaturesSe.npy")
npyDataCo2Se = np.load("Co2PlotSe.npy")
npyGlaciers = np.load("Co2mloFraction.npy")


#print(npyDataCo2Se[0])

#exit()


x = npyData[0]
y = npyData[1]
ygerr = npyData[2]
xco = npyDataCo2[0]
yco = npyDataCo2[1]
ycoerr = npyDataCo2[2]

#https://matplotlib.org/3.1.1/gallery/statistics/errorbar_features.html#sphx-glr-gallery-statistics-errorbar-features-py
lower_error = ygerr
upper_error = ygerr
asymmetric_error = [lower_error, upper_error]



#plt.ylim(0, 400)

#plt.xticks(rotation=90)
#plt.subplots_adjust(bottom=0.22)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()


ax1.errorbar(x, y, xerr=asymmetric_error, fmt='o', markersize=4, elinewidth=0.5, capsize=0, label='Global Temperature')
ax2.errorbar(xco, y=yco, yerr=ycoerr, fmt='ro', markersize=4, elinewidth=0.5, capsize=0, label='CO2 mole fraction')
ax1.legend(loc ='upper left')
ax2.legend(loc ='upper center')
plt.show()


