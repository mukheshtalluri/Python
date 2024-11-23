def sum_prod(input_tuple):
    tuple_sum = 0
    tuple_prod = 1
    for i in range(len(input_tuple)):
        tuple_sum += input_tuple[i]
        tuple_prod *= input_tuple[i]
    print(tuple_sum, tuple_prod, sep= ",")

my_tuple = (1, 2, 3, 4)
# sum_prod(my_tuple) # Time complexity - O(n) and Space complexity - O(1)

def element_wise_sum(tuple1, tuple2):
    print(tuple(map(sum, zip(tuple1, tuple2))))

tup_1 = (1, 2, 3)
tup_2 = (4, 5, 6)
# element_wise_sum(tup_1, tup_2)

def insert_at_beginning(element, tuple_1):
    tuple_1 = (element, ) + tuple_1
    print(tuple_1)

tup = (2, 3, 4, 5)
#insert_at_beginning(1, tup)

def concatenation_elements_in_tuple(my_tuple):
    output = ""
    for i in my_tuple:
        output += f"{i} "
    print(output)

tuple_1 = ("My", "name", "Mukhesh", "i am", "working", "in", "TCS")
#concatenation_elements_in_tuple(tuple_1)

def diagonal_element(my_tuple):
    diagonal = []
    for i in range(len(my_tuple)):
        diagonal.append(my_tuple[i][i])
    print(tuple(diagonal))

tuple_1 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
diagonal_element(tuple_1)







