import numpy as np
import matplotlib.pyplot as plt

a = np.array([0.39, 0.72, 1.00, 1.52, 5.20, 9.54, 19.22, 30.06, 39.48]) #distances from sun (u.a)
P = np.array([0.24, 0.62, 1.00, 1.88, 11.86, 29.46, 84.01, 164.8, 248.09]) #orbital  periods
names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

plt.figure()
plt.plot(P, a, ".") #scatter plot of period vs distance
for i in range(len(P)):
    plt.text(P[i], a[i], names[i])  #annotate each point with the corresponding planet name
# Set scale, labels, title and grid
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Period [y]")
plt.ylabel("Distance from the sun [a.u.]")
plt.grid(linestyle=':', linewidth=1)
plt.show()