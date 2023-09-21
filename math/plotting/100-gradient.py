#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

x = np.random.randn(2000) * 10
y = np.random.randn(2000) * 10
z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

# Create scatter plot
plt.scatter(x, y, c=z, cmap='viridis', label='Elevation')

# Set labels and title
plt.xlabel('x coordinate (m)')
plt.ylabel('y coordinate (m)')
plt.title('Mountain Elevation')

# Add a colorbar
cbar = plt.colorbar()
cbar.set_label('Elevation (m)')

# Display the plot
plt.show()

