fruits = ["Apple","Banana","Apple"]

# print(fruits)

# Creating List

number = []

#OR

number = list()

# OR

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

'''
Indexing
Lists use zero-based indexing.

Index

0      1       2       3

Apple Banana Orange Mango

-4     -3      -2     -1

Apple Banana Orange Mango
'''

fruits = ["Apple", "Banana", "Orange", "Mango"]

# print(fruits[0])
# print(fruits[-1])

# Modifying List
fruits[0] = "Graps"

# print(fruits)

# Slicing

# print(fruits[0::2])

# print(fruits[::-1])

'''
List Method
'''

# Append : Adds one item to the end.
number = [1,2,3]

# number.append(4)

# extend : Adds multiple items.
# number.extend([4,5,6])

# insert() : Insert at a specific position.
# number.insert(0,10)

'''
remove() : Removes the first matching value.
'''
# number.remove(3)

# If the value doesn't exist: ValueError

'''
pop() : Removes by index and returns the removed value.
'''
# number.pop(1)

'''
clear() : Removes all elements.
'''

# number.clear()

'''
reverse() : Reverses the list in-place.
'''

# number.reverse()

'''
sort()

Sorts the list in ascending order.
'''

# number.reverse()
# number.sort()

'''
Built-in Functions
max()
'''
# print(max(number))
# print(min(number))
# print(sum(number))

# print(1 in number)

# for i in number:
#     print(i)

# for index, value in enumerate(number):
#     print(index, value)

'''
List Comprehensions
A concise way to create lists.
'''

even = [i for i in range(1,11) if i % 2 == 0]
# print(even)

uppercase = [i.upper() for i in ["apple","cocunuts",'watermelon']]
# print(uppercase)

