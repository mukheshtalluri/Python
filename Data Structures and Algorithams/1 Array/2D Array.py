import numpy
my_array = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_array)

# Print all values in an array
for i in range(len(my_array)):
    for j in range(len(my_array[0])):
        print(my_array[i][j])

# Insert value into the array
my_array = numpy.insert(my_array, 3, [10, 11, 12], axis = 0)
print(my_array)

# Appending value into an array
my_array = numpy.append(my_array, [[13, 14, 15]], axis = 0) # for the vertical insertion we need to use axis = 1
print(my_array)

# Delete a row or column from the array.
my_array = numpy.delete(my_array, 4, axis = 0)
print(my_array)

array_1 = numpy.array([[1, 2, 5], [3, 4, 6]])
array_2 = numpy.array([[1, 2], [3, 4], [5, 6]])
result = numpy.array([[0, 0], [0, 0]])
for i in range(len(array_1)):
    for j in range(len(array_2[0])):
        for k in range(len(array_2)):
            result[i][j] += array_1[i][k] * array_2[k][j]
print(result)