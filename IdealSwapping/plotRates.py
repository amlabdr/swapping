import matplotlib.pyplot as plt
import numpy as np

final_distance = 300
distances = list(range(1, final_distance + 1, 10))

# Load rates from the file

rates4 = np.loadtxt('IdealSwapping/rates/4nodes.txt')


#

# Plotting the moving average curve
fig, ax = plt.subplots()
ax.set_xscale('linear')
ax.set_yscale('log')
ax.set_ylim([10 ** (0), 10 ** 5])

ax.plot(distances, rates4)

# Add labels and titles
ax.set_xlabel('Distance')
ax.set_ylabel('Rate')
ax.set_title('Rates vs. Distance')

# Show the plot
plt.show()
