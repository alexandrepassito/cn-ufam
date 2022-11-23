from math import sqrt
from pprint import pprint
import numpy as np

def cholesky(A):
    """Performs a Cholesky decomposition of A, which must 
    be a symmetric and positive definite matrix. The function
    returns the lower variant triangular matrix, L."""
    n = len(A)

    # Create zero matrix for L
    L = np.zeros_like(A)


    # Perform the Cholesky decomposition
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i,j] * L[k,j] for j in range(k))
            
            if (i == k): # Diagonal elements
                # LaTeX: l_{kk} = \sqrt{ a_{kk} - \sum^{k-1}_{j=1} l^2_{kj}}
                L[i,k] = sqrt(A[i,i] - tmp_sum)
            else:
                # LaTeX: l_{ik} = \frac{1}{l_{kk}} \left( a_{ik} - \sum^{k-1}_{j=1} l_{ij} l_{kj} \right)
                L[i,k] = (1.0 / L[k,k] * (A[i,k] - tmp_sum))
    return L
 
def forward(L, y):
    x = []
    for i in range(len(y)):
        x.append(y[i])
        for j in range(i):
            x[i]=x[i]-(L[i, j]*x[j])
        x[i] = x[i]/L[i, i]
    return x

def backward(b, a):
    n = len(a)
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k+1:n], b[k+1:n]))/a[k, k]
    return b

A = np.array([[4.0, -2.0, 2.0],
[-2.0, 10.0, -7.0], 
[2.0, -7.0, 30.0]])

B = np.array([[8.0, 11.0, -31.0]])

G = cholesky(A)
GT = G.transpose() 

print ("A:")
print(A)

print ("G:")
print(G)

print ("GT:")
print(GT)

y = forward(G,B[0])
print(y)

x = backward(y, GT)

print('x = \n', x)
