import matplotlib.pyplot as plt
import pandas as pd
import dask.dataframe as dd

# Load the datasets
df_staying_home = dd.read_csv("Trips_by_Distance.csv", dtype={'Population Staying at Home': 'float64'})
df_trips_full = dd.read_csv('Trips_Full Data.csv')

# Count the unique values for the "week" column in the staying home dataset
unique_weeks_staying_home = df_staying_home['Week'].nunique().compute()
print("Number of unique weeks in staying home dataset:", unique_weeks_staying_home)

# Group the average Population Staying at Home per week
average_population_staying_home = df_staying_home.groupby(by='Week')['Population Staying at Home'].mean().compute()
print("Average population staying at home per week:")
print(average_population_staying_home)

# Plot the histogram
plt.bar(average_population_staying_home.index, average_population_staying_home.values, color='green')
plt.xlabel('Week')
plt.ylabel('Average Number of People Staying at Home')
plt.title('Average Number of People Staying at Home per Week')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()