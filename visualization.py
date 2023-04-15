import numpy as np
import matplotlib.pyplot as plt

# Generate arrival times
arrivals = list(range(5, 601, 5))

# Calculate basic statistics
mean = np.mean(arrivals)
median = np.median(arrivals)
mode = int(np.round(np.mean([x for x in set(arrivals) if arrivals.count(x) == max([arrivals.count(y) for y in set(arrivals)])])))
variance = np.var(arrivals)
std_dev = np.std(arrivals)

# Print results
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Variance:", variance)
print("Standard deviation:", std_dev)

# Create histogram
plt.hist(arrivals, bins=20)
plt.title("Histogram of Student Arrival Times")
plt.xlabel("Arrival Time (seconds)")
plt.ylabel("Frequency")
plt.show()

# Create box plot
plt.boxplot(arrivals)
plt.title("Box Plot of Student Arrival Times")
plt.ylabel("Arrival Time (seconds)")
plt.show()
