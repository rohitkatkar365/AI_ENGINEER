'''
Create File (x)
Creates a new file.
'''

file = open(r"D:\AI Engineer1\AI Engineering\Python\FileHandling\Data\data.txt", "x+")
file.write("Hello, File Handling")
file.close()