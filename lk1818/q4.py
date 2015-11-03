import numpy
from numpy import *

# Define a class for potential Mandelbrot points. 
class mandelbrot(object):
    def __init__(self, x, y):
        self.N_max = 50
        self.some_threshold = 50
        self.x = x
        self.y = y
        self.isBelong = self.check_point()
 
    # Checks if a given point belongs to the Mandelbrot set
    def check_point(self):
        c = self.x + 1j * self.y
        z = c
        for v in range(self.N_max):
	    z = z**2 + c
        if abs(z) < self.some_threshold:
            return True
        else: 
            return False


# Do the iteration; and
# Form a 2-D boolean mask indicating which points are in the set
# The default arguments are configured so that no need for additional input
def get_mask(x_min = -2, x_max = 2, x_step = 0.01, y_min = -1.5, y_max = 1.5, y_step = 0.01):
    X = arange(x_min, x_max, x_step)
    Y = arange(y_min, y_max, y_step)
    mask = empty([len(X), len(Y)], dtype = bool)
    for i in arange(len(X)):
        for j in arange(len(Y)):
            mask[i, j] = mandelbrot(X[i], Y[j]).isBelong
    return mask









    
