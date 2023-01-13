# Lagrange Interpolation

# Importing NumPy Library
import numpy as np
from numpy.polynomial import Polynomial


def gaussElimin(a, b):
    n = len(b)

# Elimination Phase
    for k in range(0, n-1):
        for i in range(k+1, n):
           if a[i, k] != 0.0:
               lam = a[i, k]/a[k, k]
               a[i, k+1:n] = a[i, k+1:n] - lam*a[k, k+1:n]
               b[i] = b[i] - lam*b[k]
# Back substitution
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k+1:n], b[k+1:n]))/a[k, k]
    return b

# Number of unknowns
n = 3

# Making numpy array of n & n x n size and initializing 
# to zero for storing x and y value along with differences of y
x = np.zeros((n))
y = np.zeros((n))
x = [1250.0, 1000.0, 750.0]
y = [25.0, 15.0, 10.0]

# Reading interpolation point
xp = 850.0

# Set interpolated value initially to zero
yp = 0

# Implementing Lagrange Interpolation
for i in range(n):
    
    p = 1
    
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    
    yp = yp + p * y[i]    

# Displaying output
print('Interpolated value at %.3f is %.3f.' % (xp, yp))

#### 

x0 = 1250.0
x1 = 1000.0
x2 = 750.0


a = np.array([[x0**2, x0, 1.0],
             [x1**2, x1, 1.0],
             [x2**2, x2, 1.0]])

b = np.array([[25.0, 15.0, 10.0]])

c = gaussElimin(a, b[0])

print('c = \n', c)

poly  = np.poly1d(c) 

print(poly)

calc = poly(xp)

print('Interpolated value at %.3f is %.3f.' % (xp, calc))



