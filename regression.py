import numpy as np
import matplotlib.pyplot as plt
#y = ax+b
#multiplication of the matrix
# [x,1][a] = [y,1]
#      [b] 

#we start by generating the data 


x = np.arange(30)
y = 5*x + 23
#visuals
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2')
plt.show()

#we'll try to get a curve y = x^2

def linear(x,y):
    a , b = 0
    #y = ax+b


    return a , b
