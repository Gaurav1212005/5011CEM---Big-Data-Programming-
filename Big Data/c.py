import pandas as pd
import dask.dataframe as dd
import matplotlib.pyplot as plt
import time

# Define number of processors
n_processors = [10, 20]
n_processors_time = {}  # Define n_processors_time dictionary

# Task (a) and (b)
for processor in n_processors:
    start_time = time.time()

    # Task (a) using Dask
    df_staying_home = dd.read_csv("Trips_By_Distance.csv", dtype={'Population Staying at Home': 'float64'})
    unique_weeks_staying_home = df_staying_home['Week'].nunique().compute(num_workers=processor)
    average_population_staying_home = df_staying_home.groupby(by='Week')['Population Staying at Home'].mean().compute(num_workers=processor)

    # Task (b) using Pandas
    df_trips_distance = pd.read_csv("Trips_By_Distance.csv")
    df_10_25 = df_trips_distance[df_trips_distance['Number of Trips 10-25'] > 10000000]
    df_50_100 = df_trips_distance[df_trips_distance['Number of Trips 50-100'] > 10000000]

    dask_time = time.time() - start_time
    n_processors_time[processor] = dask_time

    print(f"Computation time for {processor} processors: {dask_time} seconds")

# Plotting the comparison of computation time for different numbers of processors
plt.bar(n_processors_time.keys(), n_processors_time.values(), color='skyblue')
plt.xlabel('Number of Processors')
plt.ylabel('Time (seconds)')
plt.title('Computation Time for Different Numbers of Processors')
plt.show()
