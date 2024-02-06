import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define a function that represents the original data
def fdata(x, L):
    A = L/10.0
    return 2*np.sin(2*np.pi*x/L) + x*(L-x)**2/L**3 * np.cos(x) + \
           5*x*(L-x)/L**2 + A/2 + 0.1*A*np.sin(13*np.pi*x/L)

N = 2048    # Number of data points
L = 50.0    # Length of the interval
x = np.linspace(0, L, N, endpoint=False)    # Generate N values in (0,L) interval
orig = fdata(x, L)  # Generate original data
noisy = orig + 0.5*np.random.randn(N)   # Add noise to the original data

gauss = signal.gaussian(N, 25)  # Generate a Gaussian window for convolution
norm = np.sum(gauss)
gauss = gauss/norm  # Normalize the Gaussian window
conv = signal.convolve(noisy, gauss, mode='same')   # Concolution of the signal with the gaussian window

plt.plot(x, noisy, alpha=0.5, label = "noisy")
plt.plot(x, orig, label = "original")
plt.plot(x, conv, label = "convoluted")
plt.legend()
plt.show()