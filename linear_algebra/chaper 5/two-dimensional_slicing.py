# split input and output data
from numpy import array
# define
data = array([[11, 22, 33],
             [44, 55, 66],
             [77, 88, 99]])
# separate data
x, y = data[:, :-1], data[:, -1]
print(x)
print(y)


