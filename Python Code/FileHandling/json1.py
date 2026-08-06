import json

student = {
    "name": "Alice",
    "age": 20
}

with open("./student.json", "w+") as file:
    json.dump(student, file, indent=4)
    file.seek(0)
    print(json.load(file))