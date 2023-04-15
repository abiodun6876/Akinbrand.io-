import pandas as pd
import statsmodels.api as sm

# Load data from CSV file
df = pd.read_csv('arrivaldata.csv')

# Create X and y variables
X = df[['Time']]
y = df['Number of Arrivals']

# Add constant to X variable
X = sm.add_constant(X)

# Create linear regression model
model = sm.OLS(y, X).fit()

# Print model summary
print(model.summary())
