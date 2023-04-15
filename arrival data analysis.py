import numpy as np

# Load data from file
with open('data.txt', 'r') as f:
    data = [int(line.strip()) for line in f.readlines()]

# Remove NaN values
data = int([x for x in data if not np.isnan(x)])

# Perform data analysis
mean = np.mean(data)
median = np.median(data)
mode = np.bincount(data).argmax()
variance = np.var(data)
std_dev = np.std(data)

print("Mean arrival time:", mean)
print("Median arrival time:", median)
print("Mode arrival time:", mode)
print("Variance of arrival time:", variance)
print("Standard deviation of arrival time:", std_dev)
