'''
1. Duck Typing

Duck typing is a core Python concept.

The rule is:

"If it walks like a duck and quacks like a duck, treat it as a duck."

Python doesn't care about the class.

It only cares whether the object has the required method.
'''

class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def animal_sound(animal):
    animal.speak()

d = Dog()
c = Cat()
animal_sound(d)
animal_sound(c)