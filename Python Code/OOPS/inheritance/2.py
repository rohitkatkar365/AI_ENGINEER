'''
A child class defines a method with the same name and signature as a method in the parent class, replacing the parent's 
implementation.'''

class Animal:

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


obj = Dog()

obj.sound()