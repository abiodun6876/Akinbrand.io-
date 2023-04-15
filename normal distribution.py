import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Load data from CSV file
df = pd.read_csv('data.csv')

# Calculate mean and standard deviation
mean = np.mean(df['data'])
std_dev = np.std(df['data'])

# Plot histogram to check for normal distribution
plt.hist(df['data'], bins=20)
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.show()

# Create normal probability plot
res = stats.probplot(df['data'], plot=plt)
plt.show()

# Calculate z-score and probability for a given value
value = 10
z_score = (value - mean) / std_dev
prob = norm.cdf(value, mean, std_dev)
print(f"Z-score: {z_score:.2f}")
print(f"Probability: {prob:.2%}")
