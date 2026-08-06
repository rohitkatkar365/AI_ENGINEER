# Protected Attribute
class Person:
    def __init__(self):
        self._salary = 5000

p1 = Person()
print(p1._salary)