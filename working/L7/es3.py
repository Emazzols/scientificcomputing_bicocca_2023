import multiprocessing, pathos.multiprocessing
import matplotlib.pyplot as plt
from tqdm import tqdm
import os
import time
import numpy as np

def fun(a,b):
    return a*b

a = np.random.rand(10**4)   #please, rise up the exponent to make te script slower and to highlight the multiprocessing effects
b = np.random.rand(10**4)

elapsed_time=np.empty(multiprocessing.cpu_count())  #create an array to store elapsed time for each CPU count

#loop over different number of CPU
for i in range(multiprocessing.cpu_count()):

    start_time = time.time()    #record start time

    CPUS = i+1  #number of CPUs to use

    parmap = pathos.multiprocessing.ProcessingPool(CPUS).imap   #create a ProcessingPool with the specified number of CPUs

    c = list(tqdm(parmap(fun, a, b), total=len(a))) #use tqdm to track progress of parallel map operation

    elapsed_time[i] = time.time() - start_time  #calculate the employed time

    print(f"Execution time: {elapsed_time[i]} seconds")

plt.plot(np.arange(1,multiprocessing.cpu_count()+1), elapsed_time, ".")
plt.xlabel("CPUs")
plt.ylabel("Execution time [s]")
plt.savefig("es3.pdf")
plt.show()
