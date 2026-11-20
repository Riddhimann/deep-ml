import math
import numpy as np
PI = 3.14159

def power_grid_forecast(consumption_data):
    # 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
    # 2) Perform linear regression on the detrended data.
    # 3) Predict day 15's base consumption.
    # 4) Add the day 15 fluctuation back.
    # 5) Round, then add a 5% safety margin (rounded up).
    # 6) Return the final integer.
    n= len(consumption_data)
    for i in range(n):
        consumption_data[i] = consumption_data[i] - 10 * np.sin((2*np.pi*(i+1))/10)
    x = [1,2,3,4,5,6,7,8,9,10]
    xbar = np.mean(x)
    ybar = np.mean(consumption_data)
    num=0
    denum=0
    for i in range(n):
        num += (x[i]-xbar)*(consumption_data[i]-ybar)
        denum += (x[i]-xbar)**2
    m = num/denum
    c = ybar - m*xbar

    forecast = (m*15 + c) + 10 * np.sin((2*np.pi*15)/10)
    pred = math.ceil(round(forecast)*1.05)
    return pred
    pass