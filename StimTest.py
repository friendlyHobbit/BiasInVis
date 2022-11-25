import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 
#import sklearn
import pandas as pd 


# number of data points
n_points = 100

#x = np.random.normal(5.0, 1.0, n_points)    # mean = 5.0; sd = 1.0; n points = 100
#y = np.random.normal(5.0, 1.0, n_points)   # mean = 5.0; sd = 1.0; n points = 100

#x = np.random.uniform(0, 1, n_points)
#y = np.random.uniform(0, 1, n_points)

#x = np.random.standard_exponential(n_points)
#y = np.random.standard_exponential(n_points)

#x = np.random.standard_normal(n_points)
#y = np.random.standard_normal(n_points)

x = range(50)
y = range(50) + np.random.randint(0,30,50)

# not normal distribution assumed
spear_corr = stats.spearmanr(x, y)
print("spear_corr: ", spear_corr) 

# normal distribution assumed
pear_corr = stats.pearsonr(x, y)
print("pear_corr: ", pear_corr)

plt.scatter(x, y)
plt.show()

