import pandas as pd
import matplotlib.pyplot as plt

# Load the Trips_By_Distance dataset
df_trips_distance = pd.read_csv("Trips_by_Distance.csv")

# Filter the dataset for trips with 10-25 number of trips
df_10_25 = df_trips_distance[df_trips_distance['Number of Trips 10-25'] > 10000000]

# Filter the dataset for trips with 50-100 number of trips
df_50_100 = df_trips_distance[df_trips_distance['Number of Trips 50-100'] > 10000000]

# Scatter plot for trips with 10-25 number of trips
plt.figure(figsize=(10, 6))
plt.scatter(df_10_25['Date'], df_10_25['Number of Trips 10-25'], color='blue', label='10-25 Trips')
plt.xlabel('Date')
plt.ylabel('Number of Trips')
plt.title('Number of Trips (10-25) vs Date')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Scatter plot for trips with 50-100 number of trips
plt.figure(figsize=(10, 6))
plt.scatter(df_50_100['Date'], df_50_100['Number of Trips 50-100'], color='green', label='50-100 Trips')
plt.xlabel('Date')
plt.ylabel('Number of Trips')
plt.title('Number of Trips (50-100) vs Date')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

