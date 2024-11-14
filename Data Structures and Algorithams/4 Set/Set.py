"""
Set : Set is unordered mutable data structure.
1. Set won't allow duplicates.
2. Set is un order data type since we can not able to access the elements using the index.
"""
my_set = {1, 2, 3, 4, 5, 6}
print(my_set)

# Adding element to the set. But we cont able say where it will go and save since it will un order data type.
my_set.add(7)
print(my_set)

# Pop method will remove element from the set. we cont able to say which element going remove.
my_set.pop()
print(my_set)

# Remove method will remove element based on the value.
my_set.remove(3) # What ever value we passed to remove, if it is not present we will get key error.
print(my_set)

# Discard method also will remove element based on the element value.
my_set.discard(8) # If element present it will remove otherwise it won't do anything. no exception.
print(my_set)

# Clear method will remove all elements from the set.
my_set.clear()
print(my_set)

# Difference method will give us element which are not present in the other set.
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(a.difference(b))

# Intersection method will give us the elements which are present in the both the sets.
print(a.intersection(b))

# Union method will give us all moments in the both the sets without duplicates.
print(a.union(b))

# Is disjoint method will give us True if there is no common elements in both the sets else it will print false.
print(a.isdisjoint(b))

# If a set all elements present in b then it will subset of a..
print(a.issubset(b))

# If a have all element in b then it will superset of a.
print(a.issuperset(b))

# Symmetric difference will return no elements in common.
print(a.symmetric_difference(b))

# Difference update will give a set elements which don't have in b set.
#a.difference_update(b)
print(a)

# Intersection update will return elements which are present in the both the sets.
#a.intersection_update(b)
print(a)

# Symmetric difference update will give us only unique elements in the both the sets.
#a.symmetric_difference_update(b)
print(a)

# Update method will update all elements in the both the sets.
a.update(b)
print(a)