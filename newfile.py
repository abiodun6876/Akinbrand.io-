import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV data into a Pandas DataFrame
df = pd.read_csv('arrivaldata.csv')

# Calculate basic statistics
mean = np.mean(df['Number of Arrivals'])
median = np.median(df['Number of Arrivals'])
mode = int(np.round(df['Number of Arrivals'].mode()[0]))
variance = np.var(df['Number of Arrivals'])
std_dev = np.std(df['Number of Arrivals'])

# Print results
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Variance:", variance)
print("Standard deviation:", std_dev)

# Plot a bar chart of the number of arrivals
plt.bar(df['Time'], df['Number of Arrivals'], width=5)
plt.title("Arrivals Data for Student Union Shop")
plt.xlabel("Time (minutes)")
plt.ylabel("Number of Arrivals")
plt.show()
