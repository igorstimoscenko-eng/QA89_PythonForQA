empty_list = []
mixed_list = [2,'orange',4.22,True]

fruits = ['orange', 'strawberry', 'mango']
print(fruits)
print(fruits[0])

fruits[1] = 'lemon'
print(fruits)
print(fruits[1])
list1 = ['orange','lemon']
list2 = ['shampoo','soap']
combo_list = list1 + list2
print(combo_list)
fruits = ['orange', 'strawberry', 'mango']
first, second, third = fruits
print(first)
print(second)
print(third)

fruits = ['orange', 'strawberry', 'mango']
for item in fruits:
    print(f"item in fruits: {item}")


fruits = ['orange', 'strawberry', 'mango']
for item in fruits:
    print(f"item in fruits: {item}")
correct_answers = ['orange', 'strawberry', 'mango']
user_answers = ['orange', 'strawberry', 'apple']

if correct_answers == user_answers:
    print("Correct answers")
else:
    print("Incorrect answers")