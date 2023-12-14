import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy 


# outlier calc
def calculateMahalanobis(y=None, data=None, cov=None): 
  
    y_mu = y - np.mean(data) 
    if not cov: 
        cov = np.cov(data.values.T) 
    inv_covmat = np.linalg.inv(cov) 
    left = np.dot(y_mu, inv_covmat) 
    mahal = np.dot(left, y_mu.T) 
    return mahal.diagonal()


# outlier detection
def detect_outliers(df):
    # Mahalanobis distance for each row 
    df['Mahalanobis'] = calculateMahalanobis(y=df, data=df[['x', 'y']])

    # calculate p-value for each mahalanobis distance 
    df['p'] = 1 - scipy.stats.chi2.cdf(df['Mahalanobis'], 3)

    return df


# define function to generate random scatterplots with a given correlation
def generate_data(correlation):
    # generate random x and y data with the given correlation
    mean = [0, 0]
    cov = [[1, correlation], [correlation, 1]]
    x_data, y_data = np.random.multivariate_normal(mean, cov, 600).T

    # create df to hold data
    data = {'x': x_data, 'y': y_data}
    data_df = pd.DataFrame(data, columns=['x','y'])

    # Mahalanobis distance for each row 
    detect_outliers(data_df)
    
    # Delete rows where p-value is less than 0.001
    data_df = data_df[data_df['p'] > 0.001]

    return data_df


# add outlier back in
def add_outliers(df, n_out, dist):
    # take df
    x = df["x"]
    y = df["y"]

    # find regression line (m (slope) and b(intercept) )
    m, b = np.polyfit(x, y, 1)
    # linear regression: m*x+b
    y_point = m*x+b
    print("y_point")
    print(y_point)

    plt.plot(x, m*x+b)
    
    # hold points in df
    reg_df ={'x': x_data, 'y': y_data}
    data_df = pd.DataFrame(reg_df, columns=['reg_x','reg_y'])
    



    # generate n_out points on line
    # move points in y direction
    # add points to data_df

    return df


add_outliers(generate_data(0.8), 0, 0)


# generate scatterplots with correlation values of 0.2, 0.4, and 0.6
corr = [0.8]

for c in corr:
    # get characteristics
    df = generate_data(c)

    x_data = df.loc[:, ["x"]]
    y_data = df.loc[:, ["y"]]

    # plot the scatterplot
    plt.scatter(x_data, y_data, c='#000000', s=10)
    plt.title(f"Scatterplot with Correlation = {c}")
    plt.tick_params(left = False, right = False , labelleft = False , 
                labelbottom = False, bottom = False) 
    plt.show()






