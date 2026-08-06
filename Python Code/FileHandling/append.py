'''
Append Mode (a)

Adds data without removing existing content.
'''

file = open("D:\AI Engineer1\AI Engineering\Python\FileHandling\Data\data1.txt","a+")

file.write("ML")
print(file.read())
file.close()