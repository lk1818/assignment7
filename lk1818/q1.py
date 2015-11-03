import numpy
from numpy import *

class Q1():

    def __init__(self):
        self.nrow = 5
        self.ncol = 3
        self.array = self.get_array()
        self.a = generate_1a(self.array)
        self.b = generate_1b(self.array)
        self.c = generate_1c(self.array)
        self.d = generate_1d(self.array)

    # Print arrays generated from parts of the question 
    def __repr__(self):
        str_q1 = '\nQuestion 1: \n\nGenerate a new array containing the 2nd and 4th rows: \n %s \n\nGenerate a new array that contains the 2nd column: \n %s \n\nGenerate a new array that contains all the elements in the rectangular section between the coordinates [1,0] and [3,2]: \n %s \n\nGenerate a new array that contains only elements with values that are between 3 and 11: \n %s' % (array_str(self.a), array_str(self.b), array_str(self.c), array_str(self.d))
        return str_q1


    # Declare an array with desired shape, and use a for-loop to place the elements into the array
    def get_array(self):
        arrayq1 = empty([self.nrow, self.ncol], dtype = int)
        for i in arange(self.nrow):
            arrayq1[i] = arange(i+1, i+12, 5)
        return arrayq1



# Part a. Generating a new array containing the 2nd and 4th rows.
def generate_1a(arr):
    array1a = arr[(1,3), :]
    return array1a

# Part b. Generating a new array containing the 2nd column.
def generate_1b(arr):
    array1b = arr[:, 1]
    return array1b


# Part c. Generating a new array containing all the elements in the rectangular section between [1,0] and [3,2].
def generate_1c(arr):
    array1c = arr[1:4, 0:3]
    return array1c


# Part d. Generating a new array containing only elements with value between 3 and 11.
def generate_1d(arr):
    bounds_1d = logical_and(arr >= 3, arr <= 11)
    array1d = arr[bounds_1d]
    return array1d

   




