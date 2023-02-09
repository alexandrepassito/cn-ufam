# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
  
# Importing the dataset
datas = pd.read_csv('data.csv')
datas

X = datas.iloc[:, 1:2].values
print(X)
y = datas.iloc[:, 2].values
print(y)

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin = LinearRegression()
  
lin.fit(X, y)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
  
poly = PolynomialFeatures(degree = 3)
X_poly = poly.fit_transform(X)
  
poly.fit(X_poly, y)
lin2 = LinearRegression()
lin2.fit(X_poly, y)

# Visualising the Linear Regression results
plt.scatter(X, y, color = 'blue')
  
plt.plot(X, lin.predict(X), color = 'red')
plt.title('Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
  
#plt.show()
plt.savefig("lin.png")

# Visualising the Polynomial Regression results
plt.scatter(X, y, color = 'blue')
  
plt.plot(X, lin2.predict(poly.fit_transform(X)), color = 'red')
plt.title('Polynomial Regression')
plt.xlabel('x')
plt.ylabel('y')
  
#plt.show()
plt.savefig("poly.png")

# Predicting a new result with Linear Regression after converting predict variable to 2D array
pred = 15.0
predarray = np.array([[pred]])
print(lin.predict(predarray))

# Predicting a new result with Polynomial Regression after converting predict variable to 2D array
pred2 = 15.0
pred2array = np.array([[pred2]])
print(lin2.predict(poly.fit_transform(pred2array)))
#print(141.8962 - 137.1313*pred2 + 28.500*pred2*pred2)
#print(1.0 + pred2 - 3.0*pred2*pred2 + 2*pred2*pred2*pred2)
