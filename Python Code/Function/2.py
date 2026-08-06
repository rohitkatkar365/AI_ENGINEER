#Postional Argument
def student(name,age):
    print(name,age)

# student("Rohit","23") 

#Keyword Argument
def student(name,age):
    print(name,age)

# student(age=23,name="Rohit") 

# Default Arguement
def student(name="Rohit",age=23):
    print(name,age)

# student()

# Varible_length Argument
def total(*num):
    print(sum(num))

# total(1,2,3)

# Keyword variable-length argument
def student1(**info):
    print(info)

student1(name="Rohit",age=23)

