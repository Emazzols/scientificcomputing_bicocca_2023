import numpy as np
import time

l = 10000
a = np.random.rand(l)   #Generate a random array with length 'l'

start_time = time.time()    #Initialize time
user_std = np.sqrt(np.sum((a-np.mean(a))**2)/l) #Calculate standard deviation using user method
user_time = time.time() - start_time    #Calculate user time

#Print user results (std and calculation time)
print("user std: ", user_std)
print("user time: ", user_time, "s")

start_time = time.time()    #Initialize time
numpy_std = np.std(a)   #Calculate standard deviation using numpy method
numpy_time = time.time() - start_time   #Calculate numpy time

#Print numpy results (std and calculation time)
print("numpy std: ", numpy_std)
print("numpy time: ", numpy_time, "s")
