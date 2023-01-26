import pandas as pd
import numpy as np

def newton_interpolation(x, y, xi):
    #length/number of datapoints
    n = len(x)
    #divided difference initialization
    fdd = [[None for x in range(n)] for x in range(n)]
    #f(X) values at different degrees
    yint = [None for x in range(n)]
    #error value
    ea = [None for x in range(n)]
    
    #finding divided difference
    for i in range(n):
        fdd[i][0] = y[i]
    for j in range(1,n):
        for i in range(n-j):
            fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1])/(x[i+j]-x[i])
    
    #just printing dd here
    fdd_table = pd.DataFrame(fdd)
    print(fdd_table)
    
    #interpolating xi
    xterm = 1
    yint[0] = fdd[0][0]
    for order in range(1, n):
        xterm = xterm * (xi - x[order-1])
        yint2 = yint[order-1] + fdd[0][order]*xterm
        ea[order-1] = yint2 - yint[order-1]
        yint[order] = yint2
    
    return (yint2)


x = [1250.0, 1000.0, 750.0]
y = [25.0, 15.0, 10.0]

a = newton_interpolation(x, y, 850)
print(a)
