# Sometimes, you don't want your data to be mutable
# Mutable
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_2)
print(tuple_1)

# Tuple does not support item assignment
tuple_1[0] = 'Art'

print(tuple_2)
print(tuple_1)
