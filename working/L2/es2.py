import numpy as np
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/sbu-python-summer/python-tutorial/master/day-3/sample.txt' # URL of the data file to be downloaded

file = 'sample.txt' # Local file to save the downloaded data

# Download data from the URL and save it to the local file
with urlopen(url) as response, open(file, 'wb') as towrite_file:
    towrite_file.write(response.read())

sample = np.loadtxt("sample.txt") # Load the data from the file into an array

nbin = 10
counts, bin_edges = np.histogram(sample, nbin) # create histogram from data

print(bin_edges)

# Calculate bin centers and counts for each bin
bin_centre = np.empty(nbin)
for i in range(nbin):
    bin_centre[i] = (bin_edges[i]+bin_edges[i+1])/2
    print("bin centre for the ", i, "-esimo bin is:", bin_centre[i])
    print("number of counts for the ", i, "-esimo bin is:", counts[i])

