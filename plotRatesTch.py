import matplotlib.pyplot as plt
import numpy as np

final_distance = 300
distances = list(range(1, final_distance + 1, 10))

# Load rates from the file

rates100us = np.loadtxt('rates/TCH/100us.txt')
rates1ms =   np.loadtxt('rates/TCH/1ms.txt')
rates10ms =   np.loadtxt('rates/TCH/10ms.txt')
rates100ms = np.loadtxt('rates/TCH/100ms.txt')

#

# Plotting the moving average curve
fig, ax = plt.subplots()
ax.set_xscale('linear')
ax.set_yscale('log')
ax.set_ylim([10 ** (-1), 10 ** 4])
ax.plot(distances, rates100us)
ax.plot(distances, rates1ms)
ax.plot(distances, rates10ms)
ax.plot(distances, rates100ms)
# Add labels and titles
ax.set_xlabel('Distance')
ax.set_ylabel('Rate')
ax.set_title('Rates vs. Distance')

# Show the plot
plt.show()
