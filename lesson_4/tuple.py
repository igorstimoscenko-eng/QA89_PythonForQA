numbers_tuple = (1,2,3,4,5,6,7,9)
my_tuple = ([1,2,3],['a','b','c'])

first_element = numbers_tuple[0]

nested_tuple = (1,2,(3,4),5)
print(nested_tuple[2])
print(nested_tuple[2][1])

tuple1 = (1,2,3)
tuple2 = (1,2,3)
tuple3 = (4,5,3)
print(tuple1==tuple2)
print(tuple1==tuple3)

my_tuple = (1,2,3,4,5)
print(3 in my_tuple)

for el in my_tuple:
    print(el)

i=0
while i<len(my_tuple):
    print(my_tuple[i])
    i+=1

del my_tuple
print(my_tuple)

tuple1 = (1,2,3)
tuple2 = (4,5,6)
conc_tuple = tuple1 + tuple2
print(conc_tuple)

my_tuple = (1,2,3,4,5)
length_of_tuple = len(my_tuple)
print(length_of_tuple)

max_element = max(my_tuple)
min_element = min(my_tuple)
print(max_element)
print(min_element)

sum_of_elements = sum(my_tuple)
print(sum_of_elements)