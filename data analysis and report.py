import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('arrivaldata.csv')

# Calculate basic statistics
mean = np.mean(df['Number of Arrivals'])
median = np.median(df['Number of Arrivals'])
mode = int(df['Number of Arrivals'].mode().values)
variance = np.var(df['Number of Arrivals'])
std_dev = np.std(df['Number of Arrivals'])

# Print results
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Variance:", variance)
print("Standard deviation:", std_dev)

# Create a bar chart of the arrivals by time
plt.bar(df['Time'], df['Number of Arrivals'])
plt.title("Arrivals by Time")
plt.xlabel("Time (minutes)")
plt.ylabel("Number of Arrivals")
plt.show()

# Create a line chart of the daily total arrivals
daily_total = df.groupby('Day').sum()
plt.plot(daily_total.index, daily_total['Number of Arrivals'])
plt.title("Daily Total Arrivals")
plt.xlabel("Day")
plt.ylabel("Number of Arrivals")
plt.show()

# Generate report
report = f"Arrivals Data Report\n\nMean: {mean}\nMedian: {median}\nMode: {mode}\nVariance: {variance}\nStandard deviation: {std_dev}\n\n"
report += "Arrivals by Time\n\n"
report += df[['Time', 'Number of Arrivals']].to_string(index=False)
report += "\n\nDaily Total Arrivals\n\n"
report += daily_total.to_string()

print(os.getcwd())  # check current working directory
with open('report.txt', 'w') as file:
    file.write(report)

