import numpy as np

def mean_squared_error(y, t):
    return 0.5*np.sum((y-t)**2)

t = [0, 0, 0, 0, 0, 1, 0, 0]
y = [0.1,0.2,0.05,0.0,0.0,0.9,0.2,0.3]

x = mean_squared_error( np.array(y), np.array(t) )
print(x)