# reshape 1D to 2D
from numpy import array

data = array([11, 22, 33, 44, 55])
print(data.shape)
# reshape
data_1 = data.reshape(data.shape[0], 1)
print(data_1)
print(data_1.shape)