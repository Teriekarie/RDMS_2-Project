# program to filter the even numbers and odd numbers in the list
# creating the list
list1 = [5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5,
         11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 20, 20.5]

# check
print("Original list")
print(list1)

# Because the questions requires to create an integer list between 5.5 and 20.5
# converting list1 to all integers 
# using the round() function

res = [round(float(i)) for i in list1]
print("Modidfied list is: ", res)


# count the even numbers
print("\nEven numbers count from the list:")

even_count = list(filter(lambda x: x%2 ==0, res))

print(even_count)

# count the  odd numbers from the list
print("\nOdd numbers from the list")

odd_count = list(filter(lambda x: x%2 != 0, res))

print(odd_count)

# Square every number in the list
print("\nSquare every number of the list")

square_count = list(map(lambda x: x** 2, res))

print(square_count)

# Find the cube of every number in the list
print("\nCube every number in the list")

cube_count = list(map(lambda x: x** 3, res))

print(cube_count)

