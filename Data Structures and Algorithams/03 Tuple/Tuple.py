"""
Tuple : Tuple is an ordered immutable data type.
1. Once tuple got created we cont able to change any operations to the tuple.
2. Tuples are faster compare with the lists because of immutability.
"""
my_tuple = (1, 2, 3, 4, 5)

# Count method will count the no.of times that element repeated in the tuple.
print(my_tuple.count(6))

# Index method will provide us index position of the element.
print(my_tuple.index(3))

# Tuple concatenation
my_tuple_1 = (6, 7, 8, 9, 10)
my_tuple = my_tuple + my_tuple_1 # Since tuples are immutable now memory address of the tuple is changed.
print(my_tuple)


