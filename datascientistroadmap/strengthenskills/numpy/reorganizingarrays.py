import numpy as np

before = np.array([[1,2,3,4],[5,6,7,8]])

# reshape matrix
after = before.reshape(8,1)
print('reshaped matrix (8,1): \n', after)
after = before.reshape(2,2,2)
print('reshaped matrix (2,2,2): \n', after)

# vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print('vertically stacked vectors: \n', np.vstack([v1,v2]))

# horizontal stacking vectors
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
print('horizontally stacked vectors: \n', np.hstack([h1, h2]))