import numpy as np
from sklearn.linear_model import LinearRegression

# Generate data
x = np.arange(5, 605, 5)
y = np.random.normal(10 * x + 50, scale=100)

# Reshape data
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)

# Train linear regression model
model = LinearRegression()
model.fit(x, y)

# Print model coefficients
print("Intercept:", model.intercept_[0])
print("Slope:", model.coef_[0][0])
