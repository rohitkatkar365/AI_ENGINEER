class Employee:
    def __init__(self):
        self.__salary = 0

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, val):
        if val >= 0:
            self.__salary = val
        else:
            raise ValueError("Salary cannot be negative")


e1 = Employee()

e1.salary = 50000      # Calls setter
print(e1.salary)       # Calls getter