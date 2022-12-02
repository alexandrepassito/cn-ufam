from pprint import pprint
#from numpy import array, zeros, diag, diagflat, dot
import numpy as np

def jacobi(A,b,tolerance, maxk, x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed                                                                                                                                                            
    if x is None:
        x = np.zeros(len(A[0]))
    x_old = x


    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = np.diag(A)
    #print(D)
    #print(np.diagflat(D))
    R = A - np.diagflat(D)
    #print(R)

    # Iterate for N times                                                                                                                                                                           
    for i in range(maxk):
        x = (b - np.dot(R,x)) / D
        d_k = np.amax(np.absolute(x - x_old))
        dr_k = (d_k / np.amax(np.absolute(x)))
        #print("dr_k", dr_k)
        #print("tolerance", tolerance) 
        x_old = x
        if (dr_k < tolerance):
            break
    return x


def gauss_seidel(A,b,tolerance, maxk, x=None):
    
    # Create an initial guess if needed                                                                                                                                                            
    if x is None:
        x = np.zeros(len(A[0]))
    x_old = x

    n = len(A)

    #Iterate
    for k in range(maxk):
        
        x_old  = x.copy()
  
       #Loop over rows
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i,:i], x[:i]) - np.dot(A[i,(i+1):], x_old[(i+1):])) / A[i ,i]
            
        #print(x)

    return x



A = np.array([[10.0, 2.0, 3.0],[1.0, 5.0, 1.0],[2.0, 3.0, 10.0]])
b = np.array([7.0, 8.0, 6.0])
guess = np.array([0.7, -1.6, 0.6])
tolerance = 5e-10
k = 25

sol = jacobi(A,b, tolerance, k, guess)
print("Jacobi:", sol)

sol2 = gauss_seidel(A,b, tolerance, k, guess)
print("Seidel:", sol2)
