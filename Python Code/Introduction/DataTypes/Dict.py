# student = {
#     "name" : "John",
#     "age" : 12,
#     "course" : ["Python","Gen Ai"]
# }

# print(student)

# Different Way to create dictonary
student = {}

# OR

student = dict()

student = {
    "name": "John",
    "marks": {
        "Math": 90,
        "Science": 85,
        "English": 95
    }
}

# Accessing
# print(student["name"])

# Accessing in nested dictonary
# print(student["marks"]['Science'])

'''
Using get()
Safer than square brackets.
'''
# print(student.get("name"))
# Missing Key : None
# print(student.get("gender"))
# We can set default value
# print(student.get("gender","Not Found"))

# Adding New Items
student["gender"] = "male"

# print(student)

# Updating existing value
student["marks"]["Science"] = 100
# print(student)

'''
update()
Updates one or more key-value pairs.
'''

student.update({
    "age": 21,
    "city": "Pune"
})


# Remove
# student.pop("city")

# Missing key: KeyError

'''
popitem()

Removes the last inserted key-value pair.
'''
# student.popitem()

'''
del

Delete a key.
'''
# del student["marks"]

# delete entire dictionary
# del student
# print(student)

# Dictionary Methods
# print(student.keys())
# print(student.values())
# print(student.items())

# loop in disctonary
for k,v in student.items():
    print(k,"->",v)