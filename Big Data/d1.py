import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.api as sm
from dask_ml.model_selection import train_test_split

# Read data
df_full = pd.read_csv("Trips_Full Data.csv")
df = pd.read_csv("Trips_By_Distance.csv")

# Clean data
# Select only numeric columns for filling NaN values
numeric_cols = df_full.select_dtypes(include=np.number)
df_full.fillna(numeric_cols.mean(), inplace=True)  # Replace NaN values with column means

# Convert 'Week of Date' to numeric
df_full['Week of Date'] = df_full['Week of Date'].str.split().str[-1].astype(int)

# Select features and target
x_linear = df_full[['Trips 1-25 Miles']]  # Linear Regression feature
y_linear = df['Number of Trips 5-10']  # Linear Regression target

# Remove rows with NaN values from both x_linear and y_linear
nan_indices = y_linear.isnull()
x_linear_clean = x_linear[~nan_indices]
y_linear_clean = y_linear[~nan_indices]
print("Shape of x_linear_clean:", x_linear_clean.shape)
print("Shape of y_linear_clean:", y_linear_clean.shape)

# Duplicate features to match the size of the target variable
x_linear_duplicate = np.repeat(x_linear_clean.values, len(y_linear_clean) // len(x_linear_clean), axis=0)

# Linear Regression
model_linear = LinearRegression()
model_linear.fit(x_linear_duplicate, y_linear_clean)

# Print Linear Regression results
print("Linear Regression:")
print("Coefficient of determination:", model_linear.score(x_linear_duplicate, y_linear_clean))
print("Intercept:", model_linear.intercept_)
print("Coefficient:", model_linear.coef_)

# Polynomial Regression
x_poly = df_full[['Trips 1-25 Miles', 'Week of Date']]  # Polynomial Regression features
y_poly = df['Number of Trips 5-10']  # Polynomial Regression target

poly_features = PolynomialFeatures(degree=2)
x_poly = poly_features.fit_transform(x_poly)

# Model Training and Data Separation
X_train, X_test, y_train, y_test = train_test_split(x_poly, y_poly)

# Print Polynomial Regression results
print("\nPolynomial Regression:")
model_poly = LinearRegression()
model_poly.fit(X_train, y_train)
print("Coefficient of determination:", model_poly.score(X_test, y_test))
print("Intercept:", model_poly.intercept_)
print("Coefficients:", model_poly.coef_)

# Advanced Linear Regression with Statsmodels
x_stats = sm.add_constant(df_full[['Trips 1-25 Miles']])
y_stats = df['Number of Trips 5-10']

model_stats = sm.OLS(y_stats, x_stats).fit()

# Print Statsmodels results
print("\nAdvanced Linear Regression with Statsmodels:")
print("Coefficient of determination:", model_stats.rsquared)
print("Adjusted coefficient of determination:", model_stats.rsquared_adj)
print("Regression coefficients:", model_stats.params)

# Predict response
print("Predicted response:\n", model_stats.fittedvalues)
print("Predicted response:\n", model_stats.predict(x_stats))