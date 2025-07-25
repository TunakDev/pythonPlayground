import numpy as np

# Load data from file
filedata = np.genfromtxt('data/data.txt', delimiter=',')
print('loaded txt data: \n', filedata)

# advanced indexing and boolean masking

# print boolean if value in matrix is greater than 10
print('is value in matrix > 10? \n', filedata > 10)

# print only values from matrix that are greater than 10
print('values greater than 10 from loaded data: \n', filedata[filedata > 10])

# indexing with a list
a = np.array([1,2,3,4,5,6,7,8,9])
print('print numbers at index [1,2,8]: \n', a[[1,2,8]])

# search values in array (exists)
print('is there any value in matrix with axis 0 above 10? \n', np.any(filedata > 10, axis=0))

# combined booleans
print('is the value between 10 and 20?: \n', ((filedata > 10) & (filedata < 20)))
print('is the value outside of 10 and 20?: \n', (~((filedata > 10) & (filedata < 20))))

# quiz
quizarray = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(quizarray)
print(quizarray[2:4, 0:2])
print(quizarray[[0,1,2,3],[1,2,3,4]])
print(quizarray[[0,4,5], 3:])