import matplotlib.pyplot as plt
#Importing matplotlib.pyplot as plt

# Data
science_marks = [85, 76, 92, 60, 88, 74]

# Create bar chart with width 0.1 and of color red
plt.bar(range(len(science_marks)), science_marks, width=0.1, color='red')

# Show the plot
plt.show()