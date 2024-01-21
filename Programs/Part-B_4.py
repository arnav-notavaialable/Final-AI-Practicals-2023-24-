import matplotlib.pyplot as plt

# Data lists
speed_1 = [90, 86, 84, 85, 99, 56]
speed_2 = [88, 86, 84, 85, 82, 84]

car_age1 = [5, 7, 8, 7, 2, 17]
car_age2 = [4, 8, 9, 10, 12, 7]

# Scatter plot
plt.scatter(car_age1, speed_1, label='Car Age 1')
plt.scatter(car_age2, speed_2, label='Car Age 2')

# Labels and legend
plt.xlabel('Car Age')
plt.ylabel('Speed')
plt.legend()

# Show the plot
plt.show()