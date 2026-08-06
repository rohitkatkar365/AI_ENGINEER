class student:
    def __init__(self,name):
        self.name = name # instance variable

    def display(self):
        print(f"Hello, {self.name}")

student1 = student("Ram")
student1.display()