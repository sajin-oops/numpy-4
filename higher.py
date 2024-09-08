'''
Higher Dimensional Arrays
An array can have any number of dimensions.

When the array is created, you can define the number of dimensions by using the ndmin argument.
'''

import numpy as np
a = np.array([1,2,3,4], ndmin=2)
print(a)
print("number of dimensions: ",a.ndim)

'''

[[1 2 3 4]]
number of dimensions:  2

'''