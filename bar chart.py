import matplotlib.pyplot as plt

# Generate data
arrivals = list(range(5, 601, 5))

# Create bar chart
plt.bar(arrivals, height=1, width=3)

# Set axis labels and title
plt.xlabel('Time (minutes)')
plt.ylabel('Number of students')
plt.title('Student Arrivals')

# Show plot
plt.show()
