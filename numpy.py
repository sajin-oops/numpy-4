import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# - O/P
'''
[[1 2]
 [3 4]]
[[5 6]
 [7 8]]
[[ 6  8]
 [10 12]]
[[-4 -4]
 [-4 -4]]
[[ 5 12]
 [21 32]]
[[0.2        0.33333333]
 [0.42857143 0.5       ]]
'''

#0-D ARRAY
import numpy as np
arr = np.array(42)
print(arr)

# 42

#1-D ARRAYS

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

# - O/P [1 2 3 4 5]

#2-D ARRAYS

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

#O/P -
'''
[[1 2 3]
 [4 5 6]]
'''
import numpy as np
arr = np.array([[[1,2,],[3,4],[5,6],[7,8]]])
print(arr)

''' O/P 
[[[1 2]
  [3 4]
  [5 6]
  [7 8]]]
'''


import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr)
print(type(arr))
'''
#- O/P 3D ARRAYS
[[[1 2 3]
  [4 5 6]]

 [[1 2 3]
  [4 5 6]]]
<class 'numpy.ndarray'>

'''