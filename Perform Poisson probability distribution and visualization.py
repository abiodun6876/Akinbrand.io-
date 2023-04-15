import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('arrivaldata.csv')

# Create 4x3 grid of subplots
fig, ax = plt.subplots(4, 3, figsize=(15, 15))

# Loop through each time interval and arrival rate
for i in range(4):
    for j in range(3):
        # Calculate arrival rate for this interval
        interval = (i*3+j)*10+10
        rate = df[df['Time Interval']==interval]['Number of Arrivals'].mean()

        # Calculate Poisson PMF for this arrival rate
        x = np.arange(0, 25)
        pmf = np.exp(-rate) * np.power(rate, x) / np.math.factorial(x)

        # Plot Poisson PMF on corresponding subplot
        ax[i,j].plot(x, pmf, 'bo', ms=4)
        ax[i,j].vlines(x, 0, pmf, colors='b', lw=5, alpha=0.5)
        ax[i,j].set_title(f"Time Interval {interval}, Rate {rate:.2f}")

        # Exit loop if all subplots have been created
        if i*3+j+1 == 12:
            break

plt.suptitle("Poisson Probability Mass Function for Arrival Data", fontsize=20)
plt.tight_layout()
plt.show()
