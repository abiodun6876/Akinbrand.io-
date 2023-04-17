import pandas as pd
import matplotlib.pyplot as plt

# read the dataset into a pandas dataframe
df = pd.read_csv('sales_data.csv')

# calculate total gross income for each branch and city
branch_city_income = df.groupby(['Branch', 'City'])['gross income'].sum()

# find the branch and city with the highest gross income
highest_income = branch_city_income.idxmax()
highest_income_value = branch_city_income.max()

# find the branch and city with the lowest gross income
lowest_income = branch_city_income.idxmin()
lowest_income_value = branch_city_income.min()

# get the descriptive statistics of the gross income column
stats = df['gross income'].describe()

# create a figure with subplots for each visualization
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# plot a pie chart to visualize total gross income for each branch
branch_income = df.groupby('Branch')['gross income'].sum()
axs[0, 0].pie(branch_income, labels=branch_income.index, autopct='%1.1f%%', startangle=90)
axs[0, 0].set_title('Total Gross Income by Branch')

# plot a bar chart to visualize gross income for each month by branch
monthly_income = df.groupby(['Branch', 'Date'])['gross income'].sum().unstack()
monthly_income.plot(kind='bar', ax=axs[0, 1])
axs[0, 1].set_title('Gross Income by Month and Branch')
axs[0, 1].set_xlabel('Branch')
axs[0, 1].set_ylabel('Gross Income')

# plot a histogram to visualize the distribution of gross income
df['gross income'].plot(kind='hist', bins=20, ax=axs[1, 0])
axs[1, 0].set_title('Distribution of Gross Income')
axs[1, 0].set_xlabel('Gross Income')
axs[1, 0].set_ylabel('Frequency')

# plot a boxplot to check for outliers in gross income
df.boxplot(column='gross income', ax=axs[1, 1])
axs[1, 1].set_title('Boxplot of Gross Income')
axs[1, 1].set_xlabel('Gross Income')

# add the statistics and branch/city details to the figure
fig.text(0.1, 0.9, 'Descriptive Statistics of Gross Income\n' + stats.to_string(), fontsize=10, va='top')
fig.text(0.1, 0.7, 'Branch and City with Highest and Lowest Gross Income\n' + f"Highest Gross Income: Branch {highest_income[0]}, {highest_income[1]} ({highest_income_value:.2f})\nLowest Gross Income: Branch {lowest_income[0]}, {lowest_income[1]} ({lowest_income_value:.2f})", fontsize=10)

# adjust the spacing between subplots and display the figure
plt.tight_layout()
plt.show()
