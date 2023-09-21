#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Generate y values (cubing numbers from 0 to 10)
y = np.arange(0, 11) ** 3

# Generate x values (from 0 to 10)
x = np.arange(0, 11)

# Plot y as a solid red line
plt.plot(x, y, 'r-')

# Set the x-axis range from 0 to 10
plt.xlim(0, 10)

# Add labels for clarity
plt.xlabel('X')
plt.ylabel('Y')

# Add a title
plt.title('Plot of y = x^3')

# Display the plot
plt.show()

