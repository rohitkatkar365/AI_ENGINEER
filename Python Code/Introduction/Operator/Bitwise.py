'''
| Operator | Meaning     |    
| -------- | ----------- | 
| `&`      | AND         |    
| `        | `           | 
| `^`      | XOR         |    
| `~`      | NOT         |    
| `<<`     | Left Shift  |    
| `>>`     | Right Shift |    
'''

a = 5           # 0 1 0 1 
b = 1           # 0 0 0 1
print(a & b)    # 0 0 0 1 (1)

a = 5           # 0 1 0 1 
b = 1           # 0 0 0 1
print(a ^ b)    # 0 1 0 0 (4)

print(~a) # 1 0 1 0(-6)
'''
Bitwise NOT (~) Operator in Python

Example:
a = 5
print(~a)

Output:
-6

Explanation:

Step 1: Convert the number to binary.

Decimal 5 = 00000101

Step 2: Apply the (~) operator.
The (~) operator flips every bit:
0 becomes 1
1 becomes 0

    00000101   (5)
~ = 11111010

Step 3: Interpret the result.
Python stores negative numbers using Two's Complement representation.
The binary 11111010 represents -6.

Therefore:

~5 = -6

Shortcut Formula:

~a = -(a + 1)

Example:

~5
= -(5 + 1)
= -6

More Examples:

~0  = -(0 + 1)  = -1
~1  = -(1 + 1)  = -2
~2  = -(2 + 1)  = -3
~10 = -(10 + 1) = -11
~15 = -(15 + 1) = -16

Key Point:
The (~) operator does NOT simply make a number negative.
It inverts every bit, and due to Two's Complement representation,
the result is always equal to -(number + 1).
'''

# a << n = a × (2ⁿ)
print(5 << 2) # 5 * 2 ** 2 = 20

# # a >> n = a // (2**n)
print(5 >> 2) # 5 // 4 = 1