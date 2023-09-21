#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Given data
np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# Labels for fruits and people
fruits = ['Apples', 'Bananas', 'Oranges', 'Peaches']
people = ['Farrah', 'Fred', 'Felicia']

# Colors for each fruit
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

# Create the stacked bar graph
fig, ax = plt.subplots()
bottom = np.zeros(len(people))  # Bottom position for each bar
width = 0.5  # Bar width

for i, fruit_type in enumerate(fruits):
    ax.bar(people, fruit[i], bottom=bottom, label=fruit_type, color=colors[i], width=width)
    bottom += fruit[i]

# Set labels and title
plt.xlabel('Person')
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')

# Set y-axis range and ticks
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))

# Display the legend
plt.legend()

# Display the plot
plt.show()

