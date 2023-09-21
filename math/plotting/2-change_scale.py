#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Given data
x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# Plot as a line graph
plt.plot(x, y, label='Fraction Remaining')

# Set labels and title
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of C-14')

# Set y-axis to be logarithmically scaled
plt.yscale('log')

# Set the x-axis range from 0 to 28650
plt.xlim(0, 28650)

# Display the legend
plt.legend()

# Display the plot
plt.show()
