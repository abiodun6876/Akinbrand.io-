import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('arrivaldata.csv')

# Create scatter plot of number of arrivals vs. time of arrival
plt.scatter(df['Time'], df['Number of Arrivals'], alpha=0.5)
plt.xlabel('Time of Arrival')
plt.ylabel('Number of Arrivals')
plt.title('Student Union Shop Traffic')
plt.show()

# Create histogram of number of arrivals
plt.hist(df['Number of Arrivals'], bins=15)
plt.xlabel('Number of Arrivals')
plt.ylabel('Frequency')
plt.title('Student Union Shop Traffic')
plt.show()
