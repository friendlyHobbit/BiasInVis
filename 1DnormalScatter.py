import numpy as np
import matplotlib.pyplot as plt

# generate random data with a normal distribution
mean = 0
stddev = 1
num_samples = 50
data = np.random.normal(mean, stddev, num_samples)

# create a constant y-value for all data points
y = np.ones(num_samples) * 5

# calculate the mean and distance of each data point from the mean
data_mean = np.mean(data)
dist_from_mean = np.abs(data - data_mean)
print("dist_from_mean: "+str(dist_from_mean))

# plot the scatterplot
plt.scatter(data, y, color='black', s=5)

# calculate the IQR and define the outlier threshold
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1
outlier_thresh = q3 + 1.5 * iqr

# identify outliers
outliers = data[data > outlier_thresh]

# set the color of the outliers to red
plt.scatter(outliers, y[:len(outliers)], color='red', s=10)

# remove axis labels and ticks
plt.axis('off')

plt.show()


# calculate probability of generating outliers
# the probability of generating outliers depends on the threshold used to define an outlier. 
# In the script, the outlier threshold is defined as the third quartile (Q3) plus 1.5 times the interquartile range (IQR). 
# If the data points are normally distributed, then approximately 7% of the data points should be classified as outliers using this threshold. 
# However, the actual probability of generating outliers in any given scatterplot using this script will depend on the random values generated for the data.