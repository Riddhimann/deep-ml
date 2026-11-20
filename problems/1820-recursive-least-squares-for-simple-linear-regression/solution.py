import numpy as np

def online_simple_regression(xs, ys):
    # return (N, 2) array of (w0, w1) after each point
    n=0
    dx = 0
    dy= 0
    meanx=0
    meany=0
    sxx=0
    sxy=0
    results=[]
    for x,y in zip(xs,ys):
        n+=1
        dx = x - meanx
        dy = y - meany
        
        meanx = meanx + (dx/n)
        meany = meany + (dy/n)

        sxx = sxx + dx*(x - meanx)
        sxy = sxy + dx*(y - meany)

        if sxx==0:
            w1 = 0
        else:
            w1 = sxy/sxx
        
        w0 = meany - w1*meanx

        results.append([w0,w1])
    return np.array(results,dtype = float)
    pass
