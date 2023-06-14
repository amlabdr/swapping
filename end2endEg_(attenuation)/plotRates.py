import matplotlib.pyplot as plt
import numpy as np

final_distance = 300
distances = list(range(1, final_distance + 1, 10))

# Load rates from the file

rates0db_km = np.loadtxt('end2endEg_(attenuation)/rates/0db|km.txt')
rates1db_km = np.loadtxt('end2endEg_(attenuation)/rates/1db|km.txt')
rates2db_km = np.loadtxt('end2endEg_(attenuation)/rates/2db|km.txt')



#

# Plotting the moving average curve
fig, ax = plt.subplots()
ax.set_xscale('linear')
ax.set_yscale('log')
ax.set_ylim([10 ** (0), 10 ** 5])



ax.plot(distances, rates0db_km, label='rates attenuation = 0db/km')
ax.plot(distances, rates1db_km, label='rates attenuation = 1db/km')
ax.plot(distances, rates2db_km, label='rates attenuation = 2db/km')


# Add labels and titles
ax.set_xlabel('Distance in Km')
ax.set_ylabel('Rate (entanglement per second)')
ax.set_title('Rates vs. Distance')
ax.legend()

# Show the plot
plt.show()
