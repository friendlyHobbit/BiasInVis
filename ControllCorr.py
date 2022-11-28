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


# Regression line error methof for outlier detection, returns list with outlier points
def GetRegOutlier():
    outlier_list = []

    err = np.abs(global_y - myfunc(set_x))
    outlier_list = np.greater(err, 1)

    # for each y value, calculate distance to regression line at point y
    #for y in global_y:
    #    err = np.abs(y - myfunc(set_x))
    #    if err > 1:
            #add y to list
    #        outlier_list.append(y)
    
    return outlier_list
    


# set dot color, takes numbers array, returns color 
def SetRegOutlierColor(ol):
    for i in ol:
        if i > 2:
            clr = 'red'
            return clr
        else:
            clr = 'black'
            return clr



# IQR method
# calculate outliers based on IQR, give 1 dimentional data as input
def OutlierDetector(d):
    # calculate Q1 and Q3
    q1, q3 = np.percentile(d, [25, 75])
    iqr = q3 - q1
    upperq = q3 + 1.5*iqr
    lowerq = q1 - 1.5*iqr

    # prints
#    print("q1: ", q1)
#    print("q3: ", q3)
#    print("IQR: ", iqr)
#    print("upperq: ", upperq)
#    print("lowerq: ", lowerq)

    return upperq, lowerq

#print("min set y: ", np.min(CreateScatter(stand_dev, set_x)))
#print("max set y: ", np.max(CreateScatter(stand_dev, set_x)))
#print("outlier y: ", OutlierDetector(CreateScatter(stand_dev, set_x)))
#print("outlier y: ", OutlierDetector(CreateScatter(stand_dev, set_x)))


# IQR method
# set color dependent on IQR, give upper, lower bounds and 1d data
def SetOutlierColor(u, l, d):
    for n in d:
        # if outside IQR
        if n >= u:
            clr = 'red'
            print("outlier")
            return clr
        elif n <= l:
            clr = 'red'
            print("outlier")
            return clr
        # else it´s outside IQR
        else:
            clr = 'black'
            return clr
    


# correlation coefficient
print("r: ", r)
print("pearsons corr: ", stats.pearsonr(set_x, CreateScatter(stand_dev, set_x)))


# get y points outside IQR
#upperqy, lowerqy = OutlierDetector(CreateScatter(stand_dev, set_x))
#scatter_c = SetOutlierColor(upperqy, lowerqy, CreateScatter(stand_dev, set_x))

# get x points outside IQR
#upperqx, lowerqx = OutlierDetector(set_x)
#scatter_c = SetOutlierColor(upperqx, lowerqx, set_x)

# try color outliers
#clr = SetRegOutlierColor(GetRegOutlier())
#plt.scatter(set_x, CreateScatter(stand_dev, set_x), c=clr, alpha=0.7)


outList = GetRegOutlier()
not_outList = np.logical_not(outList)

plt.scatter(set_x[not_outList], global_y[not_outList], c='green' , alpha=0.7)
plt.scatter(set_x[outList], global_y[outList], c='red' , alpha=0.7)

plt.plot(set_x, mymodel)

# Plot formatting
plt.yticks(color='w')
plt.xticks(color='w')
plt.xlabel("Drownings")
plt.ylabel("Ice-cream sales")

# check for outliers 
#plt.boxplot(CreateScatter(stand_dev, set_x))

plt.show()


