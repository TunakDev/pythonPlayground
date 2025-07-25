import numpy as np

a = np.array([1,2,3])

print('array a:', a)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])

print('array b:', b)

# print 2 cols, 3 lines
print('b.shape: ', b.shape)

# prints datatype of objects in array
print('b.dtype: ', b.dtype)

# specify dtype of objects in array
c = np.array([1,2,3], dtype='int16')
print('c.dtype: ', c.dtype)

# print size in bytes
print('a.itemsize: ', a.itemsize)

# print total size (# of elements)
print('a.size: ', a.size)

# get total bytesize
print('a.nbytes: ', a.nbytes)