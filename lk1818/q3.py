import numpy
from numpy import *

class Q3():
    def __init__(self):
        random.seed(1234)
        # Generate a 10 x 3 array of random numbers in the range [0, 1).
        self.random_array = random.rand(10, 3)
        self.closest_col = find_closest_col(self.random_array)
        self.closest_num = find_closest_num(self.random_array)
        

    def __repr__(self):
        str_q3 = '\n\nQuestion 3: \n\nGenerate a 10 x 3 array of random numbers in the range [0, 1): \n%s\n\nFind the column for each of the numbers in each row closest to 0.5: \n%s\n\nUse fancy indexing to extract the numbers into an array: \n%s' % (self.random_array, self.closest_col, self.closest_num)
        return str_q3

def find_closest_col(random_array):
    # Find the column for each of the numbers closest to 0.5
    closest_col = empty([1, random_array.shape[0]], dtype = int)
    for i in arange(random_array.shape[0]): 
        closest_col[:, i] = argsort(abs(random_array[i] - 0.5))[0]
    closest_col = tuple(closest_col.ravel())
    return closest_col

def find_closest_num(random_array):
    result_closest = random_array[arange(len(random_array)), find_closest_col(random_array)] 
    return result_closest


    
