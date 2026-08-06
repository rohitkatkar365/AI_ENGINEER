'''
| Operator | Meaning                        |
| -------- | ------------------------------ |
| `and`    | Both conditions must be True   |
| `or`     | At least one condition is True |
| `not`    | Reverses the result            |
'''

a = 10
b = 20
c  = 30

print(a > b and b < c) # 10 > 20 and 20 < 30 = False(0) and True(1) : False
print(a > b or b < c) # 10 > 20 or 20 < 30 = False(0) or True(1) : True
print(not(a > b and b < c)) # 10 > 20 and 20 < 30 = False(0) and True(1) : ~False = True