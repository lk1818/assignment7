import matplotlib.pyplot as plt
from q1 import *
from q2 import *
from q3 import *
from q4 import *

try:
    # Answer of question 1
    print(Q1())
    
    # Answer of question 2
    print(Q2())

    # Answer of question 3
    print(Q3())

    # Plot the image of question 4
    mask = get_mask()
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
    print('\n\nQuestion 4:\nSaved the result to an image named "mandelbrot.png" in current directory')


except ArithmeticError:
    pass 
except OverflowError:
    pass 
except ValueError:
    pass 
except TypeError:
    pass 
except KeyboardInterrupt:
    pass 
    
