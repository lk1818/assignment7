import numpy
from numpy import *

class Q2():

    def __init__(self):
        self.a = arange(25).reshape(5, 5)
        self.b = array([1, 5, 10, 15, 20])
        self.division = get_division(self.a, self.b)

    def __repr__(self):
        str_q2 = '\n\nQuestion 2: \n\nGiven the array: \na = np.arange(25).reshape(5, 5), \ndivide each column element-wise with the array:\nb = np.array([1., 5, 10, 15, 20]. \n\n%s' % array_str(self.division,)
        return str_q2

    

def get_division(a, b):
    # Declare an empty array where the results will be placed
    resultq2 = empty([a.shape[0], a.shape[1]], dtype = float) 

    # Adding the results the division
    for i in arange(a.shape[0]):
        for j in arange(a.shape[1]):
            resultq2[i,j] = float(a[i, j])/float(b[j])
        
    return resultq2


    
