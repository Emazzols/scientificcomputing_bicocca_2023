import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def f(x):  # Define the function of interest
    return np.exp(-x**2)

a = -5  # Define the integration limits
b = 5
I_quad, err_quad = integrate.quad(f, a, b, epsabs=1.e-10, epsrel=1.e-10)  # Integrate using the quad method

N = np.array([32, 64, 128, 256, 512, 1024, 2048, 4096])  # Define an array where each entry is the number of samples for simps
I_simps = np.zeros(len(N))
for i in range(len(N)):  # Loop over each entry in the sampling vector
    x = np.linspace(a, b, N[i], endpoint=True)  # Define the x values to be passed to the function. In each iteration, the number of x values is the number specified in the N array
    I_simps[i] = integrate.simps(f(x), x)  # Integrate using simps

err_simps = np.abs(I_simps - I_quad)  # Calculate the error of simps as the absolute difference between the integral obtained with simps and that obtained with quad (assumed to be correct)

plt.figure()
plt.plot(N, err_simps, '.')  # Plot the error as a function of the number of samples
#plt.xscale('log')
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('simps err')
plt.show()



