import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
from scipy import stats 
import pandas as pd 


# set controlled variables
n_data_points = 100
stand_dev = 4
set_corr = 0.4
#set_x = np.random.uniform(1, 20, n_data_points) 
set_x = np.random.standard_normal(n_data_points)
# error for adjusting the scatter to fit the correlation coefficient
error = 0.01

def CreateScatter(sd, x):
    temp_sd = sd
    for i in range(200):
        y = x + np.random.normal(0, temp_sd, n_data_points) # mean, sd, n data points 

        # normal distribution assumed
        # calculate correlation based on
        pear_corr, p_var = stats.pearsonr(x, y)

        # if found correlation is bigger than set correlation, increase variance; else if found correlation is smaller than set correlation, decrease variance
        if pear_corr < set_corr:
            temp_sd -= 0.05
        elif pear_corr > set_corr:
            temp_sd += 0.05

        # check if difference between target correlation and current correlation is smaller than set error
        if (np.abs(set_corr - pear_corr) < error):
            break

    return y

# save y
global_y = CreateScatter(stand_dev, set_x)     



# get regression variables
slope, intercept, r, p, std_err = stats.linregress(set_x, global_y) 


# calculate the regression line, returns y
def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, set_x))

# get prediction at given point
#predict_n = myfunc(10)
#print("predict_n: ", predict_n)



# IQR method
# calculate outliers based on IQR, give 1 dimentional data as input
def OutlierDetectorIQR(d):      # shows some outliers for x, and y
    # calculate Q1 and Q3
    q1, q3 = np.percentile(d, [25, 75])
    iqr = q3 - q1
    upperq = q3 + 1.5*iqr
    lowerq = q1 - 1.5*iqr

    # prints
#    print("q1: ", q1)
#    print("q3: ", q3)
#    print("IQR: ", iqr)
    print("upperq: ", upperq)
    print("max: ", d.max())
    print("lowerq: ", lowerq)
    print("min: ", d.min())

    # add to array: all data greater than upper and less than lower
    outlier_list = np.greater(d, upperq) & np.less(d, lowerq)
    #print("outlier_list: ", outlier_list)
    inlier_list = np.less(d, upperq) & np.greater(d, lowerq)
    #print("inlier_list: ", inlier_list)

    return upperq, lowerq, outlier_list, inlier_list


# caclulates ouliers in dataset (mean +- 3 * SD), takes dataset, returns database with outliers and outlier bound
def ThreeSDmean(d):     # shows no outliers for x, or y
    outlier_d = []

    # mean +- 3 * SD
    outlier_bound = 3 * d.std()

    # outlier bound of the data
    print("outlier_bound: ", outlier_bound)
    outlier_d = d[np.abs(d - d.mean()) > outlier_bound]

    # Size of new list with only outliers
    #print("outlier_d size: ", outlier_d.size)

    return outlier_d, outlier_bound


# investigate outliers x
#plt.boxplot(set_x)
#print("three sd away from mean:")
#ThreeSDmean(set_x)
#print("IQR method")
#OutlierDetectorIQR(set_x)

# investigate outliers y
#plt.boxplot(global_y)
#print("three sd away from mean:")
#ThreeSDmean(global_y)
#print("IQR method")
#OutlierDetectorIQR(global_y)



# Regression line error methof for outlier detection, returns list with outlier points
def GetRegOutlier():
    outlier_list = []
    outlier_criteria = 5

    # Calculate y distance of each dot to reg line
    err = np.abs(global_y - myfunc(set_x))

    # check the IQR of error point
    iqr_err_upper, iqr_err_lower = OutlierDetectorIQR(err)
    #print("Max err value: ", np.max(err))
    #print("upper IQR value: ", iqr_err_upper)
    #outlier_criteria = iqr_err_upper

    # try sd method
    outlier_set, outlier_bound = ThreeSDmean(err)
    outlier_criteria = outlier_bound

    # Only add dots list with a distance bigger than 1 ?
    outlier_list = np.greater(err, outlier_criteria)   

    #plt.boxplot(err)

    return outlier_list
    

# ----- Outliers (IQR) of X and Y ------
# calculate upper, lower bounds of x
uox, lox, outlx, inlx = OutlierDetectorIQR(set_x)
# calculate upper, lower bounds of y
uoy, loy, outly, inly = OutlierDetectorIQR(global_y)
# show
#plt.scatter(set_x[outlx], global_y[outly], c='#999999' , alpha=0.8)              # outlier
#plt.scatter(set_x[inlx], global_y[inly], c='#454545' , alpha=0.8)     # inlier

# ----- Outliers far away from regression line ------
#outList = GetRegOutlier()   # np array of bool
#not_outList = np.logical_not(outList)

# ----- Control ------
plt.scatter(set_x, global_y, c='#454545', alpha=0.7)

# ----- Dark outliers ------
#plt.scatter(set_x[not_outList], global_y[not_outList], c='#999999' , alpha=0.8)
#plt.scatter(set_x[outList], global_y[outList], c='#454545' , alpha=0.8)

# ------ light outliers ------
#plt.scatter(set_x[not_outList], global_y[not_outList], c='#454545' , alpha=0.8)
#plt.scatter(set_x[outList], global_y[outList], c='#999999' , alpha=0.8)


#plt.plot(set_x, mymodel)

# Plot formatting
plt.yticks(color='w')
plt.xticks(color='w')
plt.xlabel("Drownings")
plt.ylabel("Ice-cream sales")


# correlation coefficient
print("r: ", r)
print("pearsons corr: ", stats.pearsonr(set_x, CreateScatter(stand_dev, set_x)))


plt.show()


