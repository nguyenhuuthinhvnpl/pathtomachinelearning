# create array with vcstack
from numpy import array
from numpy import vstack
from numpy import hstack

# create first array
a1 = array([1, 2, 3])
a2 = array([4, 5, 6])

print(a1)
print(a2)

# create new array by vstack function
a3 = vstack((a1, a2))
print(a3)
print(a3.shape)

# create new array by hstack function
a4 = hstack((a1, a2))
print(a4)
print(a4.shape)