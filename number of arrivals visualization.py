import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('arrivaldata.csv')

# Create a bar chart of number of arrivals
df['Number of Arrivals'].value_counts().sort_index().plot(kind='bar')
plt.title('Number of Arrivals')
plt.xlabel('Number of Arrivals')
plt.ylabel('Frequency')
plt.show()
