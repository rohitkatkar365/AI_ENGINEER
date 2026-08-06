data = (10, "Python", 3.14, True)


# Creating Tuple
tup = ()

# OR

tup = tuple()

# OR

student = (
    ("John", 20),
    ("Alice", 21)
)

# oR
tup = 1,2,3,4

# t = (10) : <class 'int'>

#instead 
# t = (10,) : <class 'tuple'>

'''
Indexing

Tuples use zero-based indexing.
Index

0     1     2     3

10   20    30    40
-----------------------
-4   -3   -2   -1

10   20   30   40
'''
# print(len(data))

# print(data[1:])

numbers = (10, 20, 30, 20)

print(numbers.index(20))