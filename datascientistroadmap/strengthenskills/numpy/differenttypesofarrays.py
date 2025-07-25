import numpy as np

# all 0s matrix
print('all zeroes 3-d: \n', np.zeros((2,3,3)))

# all ones matrix with fix datatype
a = np.ones((2,2,2), dtype='int16')
print('all ones with specific datatype: \n', a)
print('dtype: \n', a.dtype)

# any other number
b = np.full((2,2), 99, dtype='float32')
print('full matrix of specific number with specific datatype: \n', b)
print('dtype: \n', b.dtype)

# any other number (full_like)
c = np.full_like(a, 4)
print('full matrix of 4s with same shape as matrix a: \n', c)

# array of random decimal numbers
print('matrix filled with random decimal numbers: \n', np.random.rand(4,2,3))
print('matrix filled with random decimal numbers (with parameter shape): \n', np.random.random_sample(a.shape))

# random integer (low: inclusive, high: exclusive, negative values possible)
print('random integer up to 7: \n', np.random.randint(7))
print('random integer between 4 and 7: \n', np.random.randint(4,7))
print('random integer between 4 and 7 (with parameter size): \n', np.random.randint(4,7, size=(3,3)))

# identity-matrix
print('identitiy-matrix with size 5: \n', np.identity(5))

# repeat array (2d)
arr = np.array([[1,2,3]])
print('repeated array: \n', np.repeat(arr, 3))
print('repeated array with axis 0: \n', np.repeat(arr, 3, axis=0))

# exercise
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1

array = np.zeros((5,5), dtype='int')
array[0,:] = 1
array[4,:] = 1
array[:,0] = 1
array[:,4] = 1
array[2,2] = 9
print('exercise: \n', array)

# alternative solution
array = np.ones((5,5))
innerarray = np.zeros((3,3))
innerarray[1,1] = 9
array[1:-1,1:-1] = innerarray
print('alternative solution: \n', array)

# >> be careful when copying arrays!!
i = np.array([1,2,3])
j = i
print('i: ',i)
print('j: ',j)
print('change value in j')
j[0] = 100
print('i is also changed due to \"j = i\"')
print('i: ',i)
print('j: ',j)
print('copy i to k')
print('change value in k')
k = i.copy()
k[1] = 200
print('i: ',i)
print('k: ',k)
