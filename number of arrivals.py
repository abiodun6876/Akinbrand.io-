import pandas as pd

# Load data from CSV file
df = pd.read_csv('arrivaldata.csv')

# Calculate statistics for time of arrivals
time_stats = df['Number of Arrivals'].describe()

# Print the results
print(time_stats)
