'''
Opening a File
Use the open() function.
'''

# file = open(filename, mode)
'''
| Mode   | Meaning                          |
| ------ | -------------------------------- |
| `"r"`  | Read (default)                   |
| `"w"`  | Write (overwrite)                |
| `"a"`  | Append                           |
| `"x"`  | Create new file                  |
| `"t"`  | Text mode (default)              |
| `"b"`  | Binary mode                      |
| `"r+"` | Read and write                   |
| `"w+"` | Write and read (overwrites file) |
| `"a+"` | Append and read                  |
'''

fp = open("D:\AI Engineer1\AI Engineering\Python\FileHandling\Data\data1.txt","r")
print(fp.read())

