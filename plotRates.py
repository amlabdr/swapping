import matplotlib.pyplot as plt
import numpy as np

final_distance = 300
distances = list(range(1, final_distance + 1, 10))

# Load rates from the file
rates3 = np.loadtxt('rates/3nodes.txt')
rates4 = np.loadtxt('rates/4nodes.txt')
rates5 = np.loadtxt('rates/5nodes.txt')

#

# Plotting the moving average curve
fig, ax = plt.subplots()
ax.set_xscale('linear')
ax.set_yscale('log')
ax.set_ylim([10 ** (-1), 10 ** 4])
ax.plot(distances, rates3)
ax.plot(distances, rates4)
ax.plot(distances, rates5)
# Add labels and titles
ax.set_xlabel('Distance')
ax.set_ylabel('Rate')
ax.set_title('Rates vs. Distance')

# Show the plot
plt.show()
