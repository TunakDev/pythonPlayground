import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

# get specific value [row, column] (starting at 0)
print('5th element in 2nd array: ', a[1, 5])
print('2nd element from the back in the 2nd array: ', a[1, -2])

# get a specific row
print('get first row: ', a[0,:])

# get a specific column
print('get 2nd column: ', a[:,2])

# get every 2nd number [startindex:endindex:stepsize
print('every 2nd number from array: ', a[0, 1:6:2])

# set value
a[1,5] = 20
print('set value: ', a[1,5])

# set whole column
a[:,2] = 5
print('set column (3rd col): ', a)

# set whole column with list of numbers
a[:,3] = [1,2]
print('set column (4th col): ', a)

# 3-D example
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print('3-d example: ', b)

# get specific element (work outside in - first which bracket, then which row, then which col
#  b[0] returns [[1,2],[3,4]], b[0,1] returns [3,4], b[0,1,1] returns 4
print('specific value: ',b[0,1,1])

# replace
b[:,1,:] = [[9,9],[8,8]]
print('replaced in 3-d: ',b)