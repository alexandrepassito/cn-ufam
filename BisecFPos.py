import math
from numpy import sign
from cmath import log, log10

def bisection(f,x1,x2,tol, k_max):
    y = 0

    for i in range(k_max + 1):
        x3 = 0.5*(x1 + x2); 
        if (abs(f(x3)) <= tol):
            break
        if sign(f(x1))!= sign(f(x3)): x2 = x3
        else: x1 = x3
        y = y + 1
    return x3, y

def falsePosition(f, x1,x2,e, k_max):
    y = 0

    for i in range(k_max + 1):
        x3 = (x1 *f(x2) - x2 * f(x1)) / ( f(x2) - f(x1) )
        if (abs(f(x3)) <= tol):
            break
        if sign(f(x1))!= sign(f(x3)): x2 = x3
        else: x1 = x3
        y = y + 1
    return x3, y  


tol = 2e-3
x0 = 2.0
x1 = 3.0
k_max = 100

#def f(x): return x**3 - 10.0*x**2 + 5.0  #0 - 1
def f(x): return ((x * math.log10(x)) - 1)  #2 - 3
#def f(x): return (x**2 + x - 6)  #1  - 2.5

x, y = bisection(f, x0, x1, tol, k_max)
print(f"The Bisection root is {x} in {y} steps.")
x, y = falsePosition(f, x0, x1, tol, k_max)
print(f"The False Position root is {x} in {y} steps")
