import matplotlib.pyplot as plt
import numpy as np

final_distance = 300
distances = list(range(1, final_distance + 1, 10))

# Load rates from the file

rates10us = np.loadtxt('IdealSWAPPING_(TCH)/rates/10us.txt')
rates1ms = np.loadtxt('IdealSWAPPING_(TCH)/rates/1ms.txt')
rates10ms= np.loadtxt('IdealSWAPPING_(TCH)/rates/10ms.txt')
rates100ms= np.loadtxt('IdealSWAPPING_(TCH)/rates/100ms.txt')
rates900ms = np.loadtxt('IdealSWAPPING_(TCH)/rates/900ms.txt')
rates1s= np.loadtxt('IdealSWAPPING_(TCH)/rates/1s.txt')
rates10s = np.loadtxt('IdealSWAPPING_(TCH)/rates/10s.txt')
ratesIdeal = np.loadtxt('IdealSWAPPING_(TCH)/rates/Ideal.txt')


#

# Plotting the moving average curve
fig, ax = plt.subplots()
ax.set_xscale('linear')
ax.set_yscale('log')
ax.set_ylim([10 ** (-1), 10 ** 5])

#ax.plot(distances, rates10us, label='rates10us')
ax.plot(distances, rates1ms, label='rates1ms')
#ax.plot(distances, rates10ms, label='rates10ms')
#ax.plot(distances, rates100ms, label='rates100ms')
ax.plot(distances, rates900ms, label='rates900ms')
ax.plot(distances, rates1s, label='rates1s')
#ax.plot(distances, rates10s, label='rates10s')
ax.plot(distances, ratesIdeal, label='ratesIdeal')

# Add labels and titles
ax.set_xlabel('Distance')
ax.set_ylabel('Rate')
ax.set_title('Rates vs. Distance')
ax.legend()

# Show the plot
plt.show()
