import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("Trips_Full Data.csv")

# Filter relevant columns
distance_columns = ['Date', 'Trips <1 Mile', 'Trips 1-25 Miles', 'Trips 1-3 Miles', 'Trips 10-25 Miles', 'Trips 100-250 Miles', 'Trips 25-100 Miles','Trips 25-50 Miles','Trips 250-500 Miles','Trips 3-5 Miles','Trips 5-10 Miles','Trips 50-100 Miles', 'Trips 500+ Miles']
distance_data = data[distance_columns]

# Plot the data for each distance category
plt.figure(figsize=(12, 6))

for column in distance_data.columns[1:]:
    plt.plot(distance_data['Date'], distance_data[column], label=column)

plt.title('Number of Travelers by Distance Trips Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Travelers')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(title='Distance')
plt.tight_layout()
plt.show()
