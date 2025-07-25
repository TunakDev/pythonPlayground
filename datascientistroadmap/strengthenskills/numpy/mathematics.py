import numpy as np

a = np.array([1,2,3,4])

# add to each element (works with all operators)
print('a+2: ', a + 2)

# add arrays to arrays
b = np.array([1,0,1,0])
print('a+b: ', a + b)

# to the power of 2
print('a**2: ', a ** 2)

# take sinus function of values
print('np.sin(a): \n', np.sin(a))

# >> Linear Algebra
c = np.ones((2,3))
d = np.full((3,2), 2)
# matrix multiplication (2,3) x (3,2) = (2,2)
print('matrix multiplication: \n', np.matmul(c,d))

# determinant
c = np.identity(3)
print('determinant of identity matrix is: ',np.linalg.det(c))

