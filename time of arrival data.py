import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('arrivaldata.csv')

# Create a histogram of time of arrivals
df['Time'].hist(bins=20)
plt.title('Time of Arrivals')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.show()
