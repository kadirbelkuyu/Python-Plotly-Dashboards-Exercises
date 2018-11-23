import numpy as np

my_list = [1,2,3,4,5,6,7]

array = np.array(my_list)
print(array)

a = np.arange(0,10,2)
print(a)

# Create an array of zeros
b = np.zeros((5,5))
print(b)

# Create an array of ones
c = np.ones((5,5))
print(c)

# Create an array of random integers
d = np.random.randint(0,10)
print(d)

# Create 2d matrix of random ints

e = np.random.randint(0,10,(3,3))
print(e)

f = np.linspace(0,10,100)
print(f)

# ********************** Numpy Operations *************************************

np.random.seed(101)
array2 = np.random.randint(0,100,10)

print(array2.max)
print(array2.min())
print(array2.mean())
print(array2.argmax())
print(array2.argmin())

print(array2.reshape(2,5))

# *********************** Indexing **************************

mat = np.arange(0,100).reshape(10,10)
print(mat)

row = 0
col = 1

print(mat[row,col])

# Select an entire column (all row entries of this column "col")

print(mat[:,col])
print(mat[row,:])

##### Masking #########

print(mat > 50)
print(mat[mat>50])

