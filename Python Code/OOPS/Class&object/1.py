class student:
    def __init__(self):
        print("Object Created")

    def greet(self,name):
        print(f"Hello, {name}")

student1 = student()
student1.greet("Ram")