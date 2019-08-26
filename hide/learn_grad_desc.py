# https://github.com/arturomp/coursera-machine-learning-in-python/blob/master/mlclass-ex2-004/ex2.pdf
# https://stackoverflow.com/questions/52286971/regularized-logistic-regression-in-python-andrew-ng-course?noredirect=1#comment91524735_52286971

import numpy as np
import pandas as pd
import scipy.optimize as op
import seaborn as sns


URL = ('https://raw.githubusercontent.com/TheGirlWhiteWithBandages/'
       'Machine-Learning-Algorithms/master/Logistic%20Regression/ex2data2.txt')


# Read the data and give it labels
data = pd.read_csv(URL, header=None, names=['Test1', 'Test2', 'Accepted'])


# plot dataset
# https://stackoverflow.com/questions/21654635/scatter-plots-in-pandas-pyplot-how-to-plot-by-category
df = data
df.columns = ['x1', 'x2', 'y']
# center x1 and  x2 around mean
df.loc[:,['x1', 'x2']] -= df.mean()[['x1', 'x2']]    
sns.pairplot(x_vars=["x1"], y_vars=["x2"], data=df, hue="y", size=5) 
# - when deviations for center are small, an item is accepted 
# - at some measurements there both accepted and rejected items

# Separate the features to make it fit into the mapFeature function
X1 = data['Test1'].values.T
X2 = data['Test2'].values.T
y = np.matrix(data['Accepted'].values).T

 


def mapFeature(X1, X2, degree = 6):
    
# https://github.com/arturomp/coursera-machine-learning-in-python/blob/master/mlclass-ex2-004/mlclass-ex2/mapFeature.py

# MAPFEATURE Feature mapping function to polynomial features
#
#   MAPFEATURE(X1, X2) maps the two input features
#   to quadratic features used in the regularization exercise.
#
#   Returns a new feature array with more features, comprising of 
#   X1, X2, X1.^2, X2.^2, X1*X2, X1*X2.^2, etc..
#   for a total of 1 + 2 + ... + (degree+1) = ((degree+1) * (degree+2)) / 2 columns
#
#   Inputs X1, X2 must be the same size
    dim1 = X1.shape[0]
    dim2 = sum(range(degree + 2)) # could also use ((degree+1) * (degree+2)) / 2 instead of sum
    out = np.ones([dim1, dim2]) 
    curr_column = 1
    for i in range(1, degree + 1):
        for j in range(i+1):
            out[:,curr_column] = np.power(X1,i-j) * np.power(X2,j)
            curr_column += 1
    return out


# Separate the data into training and target
X = mapFeature(X1, X2)
m, n = X.shape
# initialize theta
theta = np.matrix(np.zeros(n))

#Initialize the learningRate(sigma)
learningRate = 1


# Define the Sigmoid Function (Output between 0 and 1)
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def cost(theta, X, y, learningRate):
    # This is require to make the optimize function work
    theta = theta.reshape(-1, 1)
    error = sigmoid(X @ theta)
    first = np.multiply(-y, np.log(error))
    second = np.multiply(1 - y, np.log(1 - error))
    return np.sum((first - second)) / m + (learningRate * np.sum(np.power(theta, 2)) / 2 * m)



    
# Define the gradient of the cost function
def gradient(theta, X, y, learningRate):
    # This is require to make the optimize function work
    theta = theta.reshape(-1, 1)
    error = sigmoid(X @ theta)
    grad =  (X.T @ (error - y)) / m + ((learningRate * theta) / m)
    grad_no = (X.T @ (error - y)) / m
    grad[0] = grad_no[0]
    return grad


result = op.minimize(fun=cost, x0=theta, args=(X, y, learningRate), method='TNC', jac=gradient)
opt_theta = np.matrix(result.x)


def predict(theta, X):
    sigValue = sigmoid(X @ theta.T)
    p = sigValue >= 0.5
    return p


p = predict(opt_theta, X)
print('Train Accuracy: {:f}'.format(np.mean(p == y) * 100))
