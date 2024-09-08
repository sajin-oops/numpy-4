 '''
NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
'''

import numpy as np
a = np.array([1,2,3,4])
print(a.ndim)

b = np.array([[1,2,3,4],[3,4,5,6]])
print(b.ndim)

arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr.ndim)
print(type(arr))
'''
#- O/P Check Number of Dimensions?    
1
2
3
'''