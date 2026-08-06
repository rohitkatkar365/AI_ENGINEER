'''
The else Block
The else block runs only if no exception occurs.
'''
try:
    num = int(input())
except:
    print("Invalid Input")
else:
    print("You enterd :- ",num)
