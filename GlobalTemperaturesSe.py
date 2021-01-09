import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('nbagg')
import matplotlib.dates as mdates
import seaborn as sns
import datetime as dt

df = pd.read_csv(r"C:\Users\amanta\Documents\ClimateChange\GlobalTemperatures.csv")

#data convert
df['dt'] = pd.to_datetime(df['dt'])

df['dt'].dt.year

df['dt'].dt.month

df['year'] = df['dt'].dt.year
df['month'] = df['dt'].dt.month

df1 = df[['dt','year','month','LandAndOceanAverageTemperature']]

dfGlobal = df1[(df1['year'] >= 1900) & (df1['year'] <= 2015)]

#Checking for NaN values



#check_for_nan = dfGlobal['LandAndOceanAverageTemperature'].isnull().values.any()


#Grouping by year - count the months and mean the Temperature by year
#getting the std from average temperature

#dfGroup = dfGlobal.groupby('year','month').agg(
 #   {'LandAndOceanAverageTemperature':['mean', 'std']})
       

#dfGlobal.groupby(['dt','year','month']).mean()


#fixing the title row 
#dfGroup.columns = dfGroup.columns.droplevel(0) 

#dfGroup.reset_index(inplace=True)



sns.set_theme()

x = dfGlobal['year']
y = dfGlobal['LandAndOceanAverageTemperature']
hue = dfGlobal['month']
# Load the penguins dataset
#penguins = sns.load_dataset("penguins")

# Plot sepal width as a function of sepal_length across days
dfGlobalgroup = sns.lmplot(
    data=dfGlobal,
    x="year", y="LandAndOceanAverageTemperature", hue="month",
    height=5
)

# Use more informative axis labels than are provided by default
dfGlobalgroup.set_axis_labels("Snoot length (mm)", "Snoot depth (mm)")

plt.show()

np.save("GlobalTemperaturesSe.npy", [x, y])


