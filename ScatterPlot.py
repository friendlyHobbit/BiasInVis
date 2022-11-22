import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 

# scatterplot 1
xpoints = np.array([1, 2, 6, 8, 19, 7, 6, 2, 8, 3, 2, 4, 6, 10])
ypoints = np.array([3, 8, 1, 10, 15, 9, 8, 4, 7, 10, 14, 7, 8, 15])

#plt.scatter(xpoints, ypoints, color = 'hotpink', alpha=0.5, s=80)

# scatterplot 2
xpoints2 = np.array([2, 1, 7, 9, 6, 7, 10, 16])
ypoints2 = np.array([1, 3, 4, 10, 7, 3, 8, 5])
sizes = np.array([13, 18, 11, 40, 45, 19, 18, 14])

#plt.scatter(xpoints2, ypoints2, color='black', s=sizes)

# scatterplot 3
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

#plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
#plt.colorbar()

# scatterplot with random data points
x = np.random.normal(5.0, 1.0, 100)    # mean = 5.0; sd = 1.0; n points = 100
y = np.random.normal(10.0, 2.0, 100)   # mean = 10.0; sd = 2.0; n points = 100

slope, intercept, r, p, std_err = stats.linregress(x, y)

def func(x):
    return slope * x + intercept

mymodel = list(map(func, x))

plt.scatter(x, y)
plt.plot(x, mymodel)

plt.title("Cute points")
plt.xlabel("cats")
plt.ylabel("dogs")

plt.show()

