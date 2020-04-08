import numpy as np
import pandas as pd

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.08

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print ("m {}, b {}, cost {} iteration {}".format(m_curr,b_curr,cost, i))
data = pd.read_csv('/home/arnab/Desktop/Python_Programs/linear_regression_single_variable/viratODI.csv',sep='\t')
x = np.array(data.Matches)
y = np.array(data.Runs)
gradient_descent(x,y)
