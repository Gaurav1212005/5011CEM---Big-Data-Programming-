import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load datasets
df_trips_distance = pd.read_csv('Trips_By_Distance.csv')
df_trips_full = pd.read_csv('Trips_Full Data.csv')

# Prepare data
# For the week 32, select relevant columns and create a new dataframe
df_week_32 = pd.DataFrame({
    'Trips': df_trips_full['Trips 1-25 Miles'],
    'Number_of_Trips': df_trips_distance['Number of Trips 5-10']  # You can choose any relevant column here
})

# Clean data (remove any missing values)
df_week_32.dropna(inplace=True)

# Split data into features (X) and target variable (y)
X = df_week_32[['Trips']]  # Feature: Trips
y = df_week_32['Number_of_Trips']  # Target variable: Number of Trips

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Linear Regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict using the model on testing data
y_pred = model.predict(X_test)

# Evaluate the model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print("Training R-squared:", train_score)
print("Testing R-squared:", test_score)

# Visualize the relationship between feature and target
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.title('Number of Trips vs. Trips 1-25 Miles')
plt.xlabel('Trips 1-25 Miles')
plt.ylabel('Number of Trips')
plt.legend()
plt.show()   
