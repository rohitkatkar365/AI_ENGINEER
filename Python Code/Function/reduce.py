from functools import reduce

li = [1,2,3]

total = reduce(lambda x,y : x+y,li)
print(total)