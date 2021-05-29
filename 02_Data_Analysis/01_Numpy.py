#############################################
# NUMPY
#############################################

# Creating Numpy Arrays
# Attributes of Numpy Arrays
# Reshaping
# Index Selection
# Slicing
# Fancy Index
# Conditions on Numpy
# Mathematical Operations

# Numerical Python
# Used for scientific calculations.
# It provides high performance work on arrays / multi-dimensional arrays and matrices.
# Similar to the lists, the difference; efficient data storage and vector operations.
# It provides the opportunity to work fast (up to 50 times compared to lists) and high level (more transactions with less effort).

#############################################
# Why NumPy?
#############################################

#######################
# Low Level vs. High Level
#######################
import numpy as np
x = [1,3,5,7,9]
y = [2,4,6,8,10]
xy = []

for i in range(0, len(x)):
    xy.append(x[i] * y[i])

# Same process done with numpy
x = np.array([1,3,5,7,9])
y = np.array([2,4,6,8,10])
x * y

#############################################
# Creating Numpy Arrays
#############################################

x = np.array([1,3,5,7,9])
type(x) # numpy.ndarray
np.zeros(5, dtype = int)

# Numbers between 0-5, one-dimensional
np.random.randint(0,5,size=8)

# mean = 10, std = 4, matrix = [3,4]
np.random.normal(10,4,(3,4))

# Numbers between 0-10 are generated, matrix=[3,3]
np.random.randint(0,10,(3,3))

#############################################
# Attributes of Numpy Arrays
#############################################

# ndim: number of dimensions
# shape: number of elements per axis
# size: total number of elements
# dtype: array data type

# Generate 8 numbers between 0 and 5
a = np.random.randint(5, size=8)
a.ndim # 1
a.shape # (8,0)
a.size # 8
a.dtype # dtype('int32')

#############################################
# Reshaping
#############################################

# Generates 7 not included numbers from 1 to 7
np.arange(1,7)

# (6,0) -> reshape ->  (3,2)
np.arange(1,7).reshape((3,2))

#############################################
# Index Selection
#############################################

x = np.random.randint(10, size=(3,5))
x[1,3]
x[:,0]
x[1,:]
x[0:2, 0:1]

#############################################
# Slicing
#############################################

a = np.random.randint(5, size=(3,5))
a[:,1]
a[2,:]
a[1:2,2:3]

#############################################
# Step
#############################################

step = np.array([1,3,5,7,9,11,13,15,17,19,21])
step[1:8:3] # 1 to 8 step = 3

#############################################
# Fancy Index
#############################################

v = np.arange(0,20,2)
# v[i] -> value at index i come
v[0] # 0
v[2] # 4

catch = [2,6,7]
v[catch]

a = np.arange(0,12).reshape((4,3))
a[2,[1,2]]
a[0:2,[1,2]]

#############################################
# Conditions on Numpy
#############################################

a = np.array([2,4,6,8])

#######################
# With classical loop
#######################

ab = []
for i in a:
    if i < 4:
        ab.append(i)
print(ab)

#######################
# With Numpy
#######################

a < 5    # return True or False
a[a < 5] # return value
a[a > 5]
a[a <= 5]
a[a >= 5]

#############################################
# Mathematical Operations
#############################################

a = [2,4,6]
a = np.array([1,2,3])
a / 4
a * 5
a ** 2
a - 1

np.subtract(a,1) # a-1
np.add(a,1)      # a+1
np.mean(a)       # avg
np.sum(a)        # sum all numbers
np.min(a)
np.max(a)
np.var(a)        # variance

#######################
# Solving Equations with Two Unknowns with NumPy
#######################

# 3 * x0 + x1 = 12
# x0 + 4* x1 = 10

a = np.array([[3,1],[1,4]])
b = np.array([12,10])

np.linalg.solve(a,b)
