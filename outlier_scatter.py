import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy 
import random
import os
import csv



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
    
    # keep rows where p-value is more than 0.001
    data_df = data_df[data_df['p'] > 0.001]

    return data_df


# add outlier back in
def generate_outliers(df, dist):
    # take df
    x = df["x"]
    y = df["y"]

    # find regression line (m (slope) and b(intercept) )
    m, b = np.polyfit(x, y, 1)
    # linear regression: m*x+b
    y_point = m*x+b
    #plt.plot(x, y_point)
    
    # hold points in df
    reg_df ={'x': x, 'y': y_point}
    data_df = pd.DataFrame(reg_df, columns=['x','y'])

    # outlier df
    outlier_df = pd.DataFrame()

    rand_index = random.randint(0, len(data_df) - 1)
    rand_row = data_df.iloc[rand_index].copy()  
    rand_row['y'] += dist

    # add to df
    outlier_df = outlier_df._append(rand_row, ignore_index=True)

    # check our outlier is an outlier
    new_df = df._append(outlier_df, ignore_index=True)
    # remove 2 columns
    new_df = new_df.drop(columns=['Mahalanobis', 'p'])
    detect_outliers(new_df)
    # print rows where p-value is less than 0.001
    print("outlier:")
    print(new_df[new_df['p'] < 0.001])

    return outlier_df    




# generate scatterplots
for x in np.arange(1,4,0.05):
    # get main correlation characteristics
    c = 0.4
    df = generate_data(c)
    x_data = df.loc[:, ["x"]]
    y_data = df.loc[:, ["y"]]

    # plot the main scatterplot
    plt.scatter(x_data, y_data, c='#000000', s=10)
    
    # add outliers
    out_df = generate_outliers(df, x) 
    
    # plot outliers
    plt.scatter(out_df['x'], out_df['y'], c='red', s=10)

    # add
    plt.title(f"Scatterplot with Correlation = {c}")
    plt.tick_params(left = False, right = False , labelleft = False , 
                labelbottom = False, bottom = False) 
       
    # save plots and df
    dir_name = os.path.dirname(__file__)
    results_dir = "\Results\Outlier_output"
    f_name = 'corr_'+ str(c) + '_dist_' + str(round(x,2))
    
    # merge df with out_df
    merged_df = df._append(out_df, ignore_index=True)
    # remove 2 columns
    merged_df = merged_df.drop(columns=['Mahalanobis', 'p'])
    detect_outliers(merged_df)
    # print rows where p-value is less than 0.001
    print("df:")
    print(merged_df)
    # df to csv file
    #np.savetxt((dir_name+f_name+'.csv'), merged_df, delimiter=',', fmt='%s')
    merged_df.to_csv(os.path.join(dir_name+results_dir, f_name + '.csv'), index=False)

    # plots
    plt.savefig(dir_name+results_dir+"\p_"+f_name+"_"+".png")
    plt.close()
   






