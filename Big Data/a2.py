import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
df = pd.read_csv('Trips_Full Data.csv')

# Calculate midpoints for each distance range
distance_ranges = ['Trips <1 Mile', 'Trips 1-25 Miles', 'Trips 25-50 Miles', 'Trips 50-100 Miles', 'Trips 100-250 Miles', 'Trips 250-500 Miles', 'Trips 500+ Miles']

midpoints = []
for range_ in distance_ranges:
    range_ = range_.replace('Trips ', '')  # Remove 'Trips ' prefix
    if '<' in range_:
        low = 0  # Set low value to 0 for ranges like '<1 Mile'
        high = 1
    elif '+' in range_:
        low = int(range_.split('+')[0])  # Extract low value
        high = 1000  # Assign high value to a large number for ranges like '500+ Miles'
    else:
        range_parts = range_.split('-')
        if len(range_parts) == 1:
            low = high = int(range_parts[0])  # Handle single value ranges
        else:
            low, high = map(int, range_parts)  # Extract low and high values
    midpoint = (low + high) / 2
    midpoints.append(midpoint)

# Calculate total trips for each distance range
df['Total Trips'] = df.iloc[:, 6:].sum(axis=1)

# Calculate weighted average distance
total_weighted_distance = sum(df[range_] * midpoint for range_, midpoint in zip(distance_ranges, midpoints))
total_trips = df['Total Trips'].sum()
average_distance = total_weighted_distance.sum() / total_trips

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(midpoints, bins=7, weights=total_weighted_distance, edgecolor='black', alpha=0.7)
plt.title('Distribution of Distances People Travel When Not Staying at Home')
plt.xlabel('Distance (miles)')
plt.ylabel('Number of Trips')
plt.grid(True)
plt.show()

print("Average Distance Traveled when not staying at home:", round(average_distance, 2), "miles")
