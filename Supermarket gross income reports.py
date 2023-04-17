import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset into a pandas dataframe
df = pd.read_csv('sales_data.csv')

# Calculate total gross income for each branch and city
branch_city_income = df.groupby(['Branch', 'City'])['gross income'].sum()

# Find the branch and city with the highest gross income
highest_income = branch_city_income.idxmax()
highest_income_value = branch_city_income.max()

# Find the branch and city with the lowest gross income
lowest_income = branch_city_income.idxmin()
lowest_income_value = branch_city_income.min()

# Get the descriptive statistics of the gross income column
stats = df['gross income'].describe()

# Create a figure with two subplots: pie chart and bar chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot a pie chart to show total gross income for each branch
colors = ['tab:blue', 'tab:green', 'tab:orange']
ax1.pie(branch_city_income, labels=branch_city_income.index, colors=colors, autopct='%1.1f%%')
ax1.set_title('Total Gross Income by Branch', fontsize=14)

# Plot a bar chart to show gross income by branch and month
monthly_income = df.groupby(['Branch', 'Date'])['gross income'].sum().unstack()
monthly_income.plot(kind='bar', ax=ax2)
ax2.set_xlabel('Branch', fontsize=12)
ax2.set_ylabel('Gross Income', fontsize=12)
ax2.set_title('Gross Income by Branch and Month', fontsize=14)
ax2.legend(title='Month', fontsize=10)

# Write the descriptive statistics and branch/city with highest/lowest gross income to a report file
with open('report.html', 'w') as f:
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<title>Sales Data Analysis Report</title>\n')
    f.write('<style>\n')
    f.write('table {border-collapse: collapse;}\n')
    f.write('table, th, td {border: 1px solid black; padding: 5px;}\n')
    f.write('</style>\n')
    f.write('</head>\n')
    f.write('<body>\n')
    f.write('<h1 style="text-align: center;">Sales Data Analysis Report</h1>\n')
    f.write('<hr />\n')
    f.write('<h2>Descriptive Statistics of Gross Income</h2>\n')
    f.write(stats.to_frame().to_html(border=0, index=False))
    f.write('<br />\n')
    f.write('<h2>Branch and City with Highest and Lowest Gross Income</h2>\n')
    f.write('<table>\n')
    f.write('<tr><th>Branch</th><th>City</th><th>Gross Income</th></tr>\n')
    f.write(f'<tr><td>{highest_income[0]}</td><td>{highest_income[1]}</td><td>${highest_income_value:.2f}</td></tr>\n')
    f.write(f'<tr><td>{lowest_income[0]}</td><td>{lowest_income[1]}</td><td>${lowest_income_value:.2f}</td></tr>\n')
    f.write('</table>\n')
    f.write('</body>\n')
    f.write('</html>\n')

# Show the plots
plt.show()
