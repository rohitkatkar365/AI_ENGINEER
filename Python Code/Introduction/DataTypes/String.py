str = "Ram"
print(type(str))

# Immutable
# str[0] = "S"
'''
Traceback (most recent call last):
  File "d:\AI Engineer1\AI Engineering\Python\Introduction\DataTypes\String.py", line 5, in <module>
    str[0] = "R"
    ~~~^^^
TypeError: 'str' object does not support item assignment
'''
# print(str)

'''
Length of String
Use len().
'''

print(len(str)) # 3

'''
1. Indexing
Each character has a position called an index.

Example:
P  y  t  h  o  n
0  1  2  3  4  5

P  y  t  h  o  n
-6 -5 -4 -3 -2 -1
'''

word = "Python"

# print(word[0])
# print(word[len(word)-1])
# print(word[-1])

'''
Slicing : 
string[start:stop:step]
'''

# print(word[0:5:1])
# print(word[-1::-1])
# print(word[-1:-3:-1])
# print(word[::-1])

'''
3. Concatenation
Joining strings using +.
'''

s1 = "Ram"
s2 = "Laxman"

# print(s1 +" "+ s2)

# Repeating Strings
# print("Hi "*3)

name = "John"

age = 20

# print(f"My name is {name} and I am {age} years old.")

# String Method

'''
upper()
Converts to uppercase.
'''
text = "Python"
print(text.upper())

'''
lower()
Converts to lowercase.
'''
print(text.lower())

'''
title()
'''
text = "python programming"
print(text.title())

'''
capitalize()
'''
print("ram".capitalize())

'''
swapcase()
'''
print(text.swapcase())

'''
split()
Splits a string into a list.
'''

t = "A B C"
print(t.split())

'''
join()
Joins a list into a string.
'''

names = ["Ram","Laxman","Arjun","Krishna"]
print("-".join(names))

'''
join()
Joins a list into a string.
'''

text = "I like Java"
print(text.replace("Java", "Python"))

'''
find()
Returns the first index of a substring.
'''

text = "Python Programming"
print(text.find("Pro"))

'''
count()
Counts occurrences.
'''

text = "banana"

print(text.count("a"))

'''
strip()

Removes leading and trailing spaces.
'''

text = "   Python   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

'''
startswith()
'''

print(text.startswith(" "))

'''
endswith()
'''

print(text.endswith(" "))