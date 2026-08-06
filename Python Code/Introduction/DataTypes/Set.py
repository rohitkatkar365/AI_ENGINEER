numbers = {10, 20, 20, 30, 40, 40}

# print(numbers)

s1 = set()
s2 = set()

'''
add()
Adds a single element.
'''
s1.add(1)
s2.add(2)
# print(s1," ",s2)

'''
update()
Adds multiple elements.
'''
s1.update([3,4])
s2.update([5,6])
# print(s1,s2)

'''
remove()
Removes a specific element.
'''
s1.remove(4)
# print(s1)

# If not value exist in set : KeyError

'''
discard()
Also removes an element.
Difference:
If the element doesn't exist, no error occurs.
'''

s1.discard(6)
# print(s1)

'''
pop()
Removes and returns an arbitrary element.
'''
numbers1 = {10, 20, 30}
x = numbers1.pop()
print(x)

'''
clear()
Removes all elements.
'''

# numbers.clear()

# Set Operations

# Union (| or union())
# Combines all unique elements.

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

'''
Intersection (& or intersection())
Common elements only.
'''
print(a & b)

'''
Difference (- or difference())
Elements in the first set but not in the second.
'''
print(a - b)

'''
Symmetric Difference (^ or symmetric_difference())
Elements present in either set, but not both.
'''

print(a ^ b)

'''
Frozen Set
A frozenset is an immutable set.
'''

fs = frozenset([1, 2, 3])

print(fs)

# Set comprehension
s  = {x for x in range(1,11)}
print(s)