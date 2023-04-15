import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('arrivaldata.csv')

# Calculate mean and standard deviation
mean = np.mean(df['Number of Arrivals'])
std_dev = np.std(df['Number of Arrivals'])

# Define time intervals and number of arrivals
time_intervals = [10, 20, 30]
num_arrivals = [3, 5, 7]

# Create 3x3 grid of subplots
fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(12, 12))

# Loop over time intervals
for i, t in enumerate(time_intervals):
    
    # Loop over number of arrivals
    for j, n in enumerate(num_arrivals):
        
        # Calculate z values
        z_values = (df[df['Time Interval'] == t]['Number of Arrivals'].values - mean) / std_dev
        
        # Plot arrival times vs. z values
        axs[i,j].scatter(df[df['Time Interval'] == t]['Number of Arrivals'], z_values, alpha=0.5)
        axs[i,j].set_title(f"Time Interval: {t}, Number of Arrivals: {n}")
        axs[i,j].set_xlabel("Number of Arrivals")
        axs[i,j].set_ylabel("z Value")

plt.tight_layout()
plt.show()
