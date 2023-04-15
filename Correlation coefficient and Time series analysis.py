import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('student_union_shop_data.csv')

# Convert 'Time' column to datetime
data['Time'] = pd.to_datetime(data['Time'])

# Set 'Time' column as index
data = data.set_index('Time')

# Plot the time series of number of arrivals
plt.figure(figsize=(10, 5))
plt.plot(data['Number of Arrivals'])
plt.title('Number of Arrivals over Time')
plt.xlabel('Time')
plt.ylabel('Number of Arrivals')
plt.show()

# Calculate and plot the autocorrelation of number of arrivals
autocorr = data['Number of Arrivals'].autocorr()
plt.figure(figsize=(10, 5))
plt.acorr(data['Number of Arrivals'], maxlags=50)
plt.title(f'Autocorrelation of Number of Arrivals (lag={autocorr:.2f})')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.show()

# Calculate and plot the correlation matrix
corr = data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
