import random
import numpy as np
import matplotlib.pyplot as plt

# define function to generate random scatterplots with a given correlation
def generate_scatterplot(correlation):
    # generate random x and y data with the given correlation
    mean = [0, 0]
    cov = [[1, correlation], [correlation, 1]]
    x_data, y_data = np.random.multivariate_normal(mean, cov, 50).T

    # find indices of obvious outliers
    x_outliers = np.where(np.logical_or(x_data < -2, x_data > 2))[0]
    y_outliers = np.where(np.logical_or(y_data < -2, y_data > 2))[0]
    outlier_indices = np.union1d(x_outliers, y_outliers)

    # remove obvious outliers
    x_data = np.delete(x_data, outlier_indices)
    y_data = np.delete(y_data, outlier_indices)

    # plot the scatterplot
    plt.scatter(x_data, y_data)
    plt.title(f"Scatterplot with Correlation = {correlation}")
    plt.show()

# generate scatterplots with correlation values of 0.2, 0.4, and 0.6
correlations = [0.2, 0.4, 0.6]
for corr in correlations:
    generate_scatterplot(corr)
