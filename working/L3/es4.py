import numpy as np
from urllib.request import urlopen
import matplotlib.pyplot as plt

#download data and save it into a txt file
url = 'https://raw.githubusercontent.com/sbu-python-summer/python-tutorial/master/day-4/nasa-giss.txt'

file = 'nasa-giss.txt'

with urlopen(url) as response, open(file, 'wb') as towrite_file:
    towrite_file.write(response.read())

#load data from file
nasa = np.loadtxt("nasa-giss.txt")

#plot temperature change over the years
plt.figure()
plt.plot(nasa[:,0], nasa[:,2])
plt.xlabel("Year")
plt.ylabel("Temperature change [°]")

colors = np.where(nasa[:,1] >= 0, "red", "blue") #different colors for positive and negative temperature changes

#plot temperature change over the years with different colors
plt.figure()
for i in range(len(nasa)):
    plt.plot(nasa[i, 0], nasa[i, 1], '.', color=colors[i])
plt.xlabel("Year")
plt.ylabel("Temperature change [°]")

plt.show()