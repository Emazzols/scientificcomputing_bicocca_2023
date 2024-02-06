import numpy as np
from scipy.stats import norm
import cProfile 
from numba import jit

@jit    #remove this to see how slower the code is. I added this after profiling the code.
def gaussian_estimators(mean, std): #function to calculate gaussian estimators
    np.random.seed(42) 
    sample_size = 10**7 #increase this to solw done the code
    gaussian_sample = np.random.normal(mean, std, sample_size)

    sample_var = np.var(gaussian_sample, ddof=1)
    sample_skewness = np.mean(((gaussian_sample - mean) / std) ** 3)
    sample_kurtosis = np.mean(((gaussian_sample - mean) / std) ** 4)
    sample_median = np.median(gaussian_sample)
    sample_mode = norm.pdf(np.linspace(min(gaussian_sample), max(gaussian_sample), 1000), loc=mean, scale=std).argmax() #this scipy method causes troubles with njit, so I used jit

    return {
        'Sample Variance': sample_var,
        'Sample Skewness': sample_skewness,
        'Sample Kurtosis': sample_kurtosis,
        'Sample Median': sample_median,
        'Sample Mode': sample_mode,
    }

mean = 0
std = 1
estimators_result = gaussian_estimators(mean, std)

for key, value in estimators_result.items():
    print(f"{key}: {value}")

cProfile.run('gaussian_estimators(mean, std)', sort='cumtime')