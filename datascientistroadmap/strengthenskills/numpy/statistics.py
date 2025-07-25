import numpy as np
stats = np.array([[1,2,3],[4,5,6]])

# minimum
print('minimum of matrix: ', np.min(stats))

# maximum over specific axis
print('maximum of matrix: ', np.max(stats, axis=0))

# sum over whole matrix
print('sum over matrix: ', np.sum(stats))
print('sum over matrix (with axis parameter): ', np.sum(stats, axis=0))