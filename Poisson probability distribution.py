import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Load data from CSV file
df = pd.read_csv('arrivaldata.csv')

# Define the time intervals
time_intervals = [10, 20, 30]

# Define the arrival rates (lambda values)
arrival_rates = [3, 5, 7, 9]

# Create a 4x3 grid of subplots
fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(12, 12))

# Loop over the arrival rates
for i, rate in enumerate(arrival_rates):

    # Loop over the time intervals
    for j, t in enumerate(time_intervals):
        
        # Calculate the Poisson probability distribution
        x = np.arange(0, 20)
        poisson_dist = poisson.pmf(x, rate*t)
        
        # Plot the Poisson probability distribution
        axs[i,j].plot(x, poisson_dist, 'bo', ms=8)
        axs[i,j].vlines(x, 0, poisson_dist, colors='b', lw=5)
        axs[i,j].set_title(f"Arrival Rate: {rate}, Time Interval: {t}")
        axs[i,j].set_xlabel('Number of Arrivals')
        axs[i,j].set_ylabel('Probability')

plt.tight_layout()
plt.show()
