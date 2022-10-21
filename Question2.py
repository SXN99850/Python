import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./data.csv")
data.head()

#Show the basic statistical description about the data.
print("Basic statistical description\n", data.describe(), "\n")

#Check if the data has null values. a. Replace the null values with the mean
print("Null value check before replacing \n", data.isnull().any(), "\n")
data.fillna(data.mean(), inplace=True)
print("Null value check after replacing \n", data.isnull().any(), "\n")

#Select at least two columns and aggregate the data using: min, max, count, mean.
aggregate_data = data.agg({'Duration':['min','max','count','mean'],'Calories':['min','max','count','mean']})
print("aggregate data \n", aggregate_data, "\n")

#Filter the dataframe to select the rows with calories values between 500 and 1000.
filtered_Data = data.loc[(data['Calories']>500)&(data['Calories']<1000)]
print("Calories data between 500 and 1000 \n", filtered_Data, "\n")

# 6. Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
filtered_Data = data.loc[(data['Calories']>500)&(data['Pulse']<100)]
print("Calories data greater than 500 and pulse less than 100 \n", filtered_Data, "\n")

# 7. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.
df_modified = data[['Duration','Pulse','Calories']]
print("modified dataframe with allcolumns except Maxpulse \n", df_modified.head(), "\n")

# 8. Delete the “Maxpulse” column from the main df dataframe
new_data = data.drop('Maxpulse', axis=1)
print("After deleting the Maxpulse column \n", new_data.head(), "\n")

# 9. Convert the datatype of Calories column to int datatype.
print("datatypes before conversion \n ",data.dtypes, "\n")
data['Calories'] = data['Calories'].astype(int)
print("datatypes after conversion \n ",data.dtypes, "\n")

# 10. Using pandas create a scatter plot for the two columns (Duration and Calories).
data.plot.scatter(x='Duration',y='Calories',c='DarkBlue')
plt.show()