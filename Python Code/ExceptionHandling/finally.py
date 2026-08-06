'''
The finally Block

The finally block always executes, whether an exception occurs or not.
'''
try:
    print("Opening file")
    result = 10 / 2

except ZeroDivisionError:
    print("Error")

finally:
    print("Closing file")