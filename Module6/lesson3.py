import numpy as np

array = np.arange(101)

# print(array)
# program to inculde range between 1 and 100
array = np.arange(1, 101)

print(array)

# program to find the even numbers
array = np.arange(0, 101, 2)

print(array)

# program to find the lcm of the even numbers
x = np.lcm.reduce(array)

print(x)


