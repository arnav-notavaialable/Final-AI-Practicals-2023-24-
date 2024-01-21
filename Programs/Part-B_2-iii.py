import matplotlib.pyplot as plt

# Data
science_marks = [85, 76, 92, 60, 88, 74]

# Create bar chart
plt.bar(range(len(science_marks)), science_marks, width=0.1, color='red')

# Set title and adjust its properties
plt.title('BAR CHART', fontsize=30, color='yellow')

# Show the plot
plt.show()