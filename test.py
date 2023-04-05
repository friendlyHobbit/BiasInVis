import numpy as np
import matplotlib.pyplot as plt

# generate and save 10 scatterplots
for i in range(10):
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

    # save dist_from_mean to a text file
    np.savetxt(f'dist_from_mean_{i}.txt', dist_from_mean)

    # plot the scatterplot with outliers marked in red
    plt.scatter(data, y, color='black', s=10)
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    outlier_thresh = q3 + 1.5 * iqr
    outliers = data[data > outlier_thresh]
    plt.scatter(outliers, y[:len(outliers)], color='red', s=10)
    plt.axis('off')
    plt.savefig('scatterplot_with_outliers_red_{}.png'.format(i))
    plt.clf()

    # plot the scatterplot with outliers marked in black
    plt.scatter(data, y, color='black', s=10)
    non_outliers = data[data <= outlier_thresh]
    plt.scatter(non_outliers, y[:len(non_outliers)], color='black', s=5)
    plt.axis('off')
    plt.savefig('scatterplot_with_outliers_black_{}.png'.format(i))
    plt.clf()
