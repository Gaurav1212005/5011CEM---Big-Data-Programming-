import time
import pandas as pd
import dask.dataframe as dd

# Define the file paths for data loading
file_path_distance = "Trips_By_Distance.csv"

# Sequential Data Processing using Pandas
start_time_pandas = time.time()

# Load data into Pandas DataFrame
df_pandas = pd.read_csv("Trips_Full Data.csv")

# Perform data analysis sequentially using Pandas
# Count the unique values for the "Week" column
unique_weeks_pandas = df_pandas['Week'].nunique()

# Group by the "Week" column and calculate the average population staying at home
average_home_population_pandas = df_pandas.groupby('Week')['Population Staying at Home'].mean()

# Group by the "Week" column and calculate the mean number of trips in the specified distance range
average_trips_distance_pandas = df_pandas.groupby('Week')['Trips 1-25 Miles'].mean()

# Measure the time taken for sequential processing using Pandas
processing_time_pandas = time.time() - start_time_pandas

# Parallel Data Processing using Dask
start_time_dask = time.time()

# Load data into Dask DataFrame
df_dask = dd.read_csv(file_path_distance)

# Perform data analysis in parallel using Dask
# Count the unique values for the "Week" column
unique_weeks_dask = df_dask['Week'].nunique().compute()

# Group by the "Week" column and calculate the average population staying at home
average_home_population_dask = df_dask.groupby('Week')['Population Staying at Home'].mean().compute()

# Group by the "Week" column and calculate the mean number of trips in the specified distance range
average_trips_distance_dask = df_dask.groupby('Week')['Trips 1-25 Miles'].mean().compute()

# Measure the time taken for parallel processing using Dask
processing_time_dask = time.time() - start_time_dask

# Compare processing times and computational efficiency
print("Sequential Processing Time (Pandas):", processing_time_pandas)
print("Parallel Processing Time (Dask):", processing_time_dask)
