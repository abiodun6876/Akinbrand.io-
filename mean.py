import pandas as pd

# Load data from csv file
df = pd.read_csv('data.csv')

# Calculate basic statistics
mean = df['Number of Arrivals'].mean()
median = df['Number of Arrivals'].median()
mode = df['Number of Arrivals'].mode()[0]
variance = df['Number of Arrivals'].var()
std_dev = df['Number of Arrivals'].std()

# Print results
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Variance:", variance)
print("Standard deviation:", std_dev)

# Write report to file
with open('report.txt', 'w') as file:
    file.write(f"Mean: {mean}\n")
    file.write(f"Median: {median}\n")
    file.write(f"Mode: {mode}\n")
    file.write(f"Variance: {variance}\n")
    file.write(f"Standard deviation: {std_dev}\n")
