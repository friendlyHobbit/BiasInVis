import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
from scipy import stats 
import pandas as pd 


# set controlled variables
n_data_points = 100
stand_dev = 4
set_corr = 0.4
set_x = np.random.uniform(1, 20, n_data_points) 

error = 0.01

def CreateScatter(sd, x):
    temp_sd = sd
    for i in range(200):
        #print("i: ", i)
        #x = np.random.uniform(1, 20, n_data_points) 
        y = x + np.random.normal(0, temp_sd, n_data_points) # mean, sd, n data points 

        # normal distribution assumed
        # calculate correlation based on
        pear_corr, p_var = stats.pearsonr(x, y)
        #print("pear_corr: ", pear_corr)

        # if found correlation is bigger than set correlation, increase variance; else if found correlation is smaller than set correlation, decrease variance
        if pear_corr < set_corr:
            temp_sd -= 0.05
        elif pear_corr > set_corr:
            temp_sd += 0.05

        # check if difference between target correlation and current correlation is smaller than set error
        if (np.abs(set_corr - pear_corr) < error):
            break

    return y
    

# get regression variables
slope, intercept, r, p, std_err = stats.linregress(set_x, CreateScatter(stand_dev, set_x))

# calculate the regression line
def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, set_x))

# get prediction at given point
#predict_n = myfunc(10)
#print("predict_n: ", predict_n)


# calculate outliers based on IQR, give 1 dimentional data as input
def OutlierDetector(d):
    # calculate Q1 and Q3
    q1, q3 = np.percentile(d, [25, 75])
    iqr = q3 - q1
    upperq = q3 + 1.5*iqr
    lowerq = q1 - 1.5*iqr

    return upperq, lowerq

print("outlier x: ", OutlierDetector(set_x))
#print("outlier y: ", OutlierDetector(CreateScatter(stand_dev, set_x)))


# set color dependent on IQR, give upper, lower bounds and 1d data
def SetOutlierColor(u, l, d):
    for n in d:
        # if outside IQR
        if n > u:
            clr = '#1f77b4'
        elif n < l:
            clr = '#1f77b4'
        # else it´s outside IQR
        else:
            clr = '#bcbd22'
    return clr



# for each x value, calculate distance to regression line
for y in CreateScatter(stand_dev, set_x):
    err = np.abs(y - myfunc(y))
    #print(err) 


# correlation coefficient
print("r: ", r)
print("pearsons corr: ", stats.pearsonr(set_x, CreateScatter(stand_dev, set_x)))
print("slope: ", slope)


# get x points outside IQR
upperqx, lowerqx = OutlierDetector(set_x)

plt.scatter(set_x, CreateScatter(stand_dev, set_x), c=SetOutlierColor(upperqx, lowerqx, set_x), alpha=0.7)
plt.plot(set_x, mymodel)

# Plot formatting
plt.yticks(color='w')
plt.xticks(color='w')
plt.xlabel("Drownings")
plt.ylabel("Ice-cream sales")


plt.show()
#plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
#plt.colorbar()


