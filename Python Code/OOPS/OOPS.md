# What is Object-Oriented Programming (OOP)?

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code using **objects**.

An **object** is an instance of a **class**.

Think of it like this:

* **Class** → Blueprint
* **Object** → Real object created from the blueprint

Class → Car

Objects

BMW
Audi
Tesla
Toyota

# Why Learn OOP?

Benefits:

* ✅ Reusable code
* ✅ Easy maintenance
* ✅ Better organization
* ✅ Real-world modeling
* ✅ Scalable applications

# Class

A **class** defines the properties (attributes) and behaviors (methods) of objects.

class ClassName:
pass

# Object

An object is created from a class.

class Student:
pass

student1 = Student()
student2 = Student()

print(student1)
print(student2)

# Constructor (`__init__`)

The constructor is automatically called when an object is created.

class Student:
def __init__(self):
print("Object created")

# `self`

`self` refers to the **current object**.

class Student:
def __init__(self, name):
self.name = name

student = Student("Alice")

print(student.name)

# Instance Variables

An **instance variable** is a variable that belongs to a **specific object (instance)** of a class. Each object has its **own copy** of the instance variables.

class Student:
def __init__(self, name, age):
self.name = name      # Instance variable
self.age = age        # Instance variable

# Instance Methods

Functions inside a class.

class Student:

def __init__(self, name):
self.name = name

def display(self):
print("Name:", self.name)
student = Student("John")

student.display()

# Class Variables

Shared among all objects.

class Student:

school = "ABC School"

def __init__(self, name):
self.name = name
student1 = Student("Alice")
student2 = Student("Bob")

print(student1.school)
print(student2.school)

# Four Pillars of OOP

<pre class="overflow-visible! px-0!" data-start="3792" data-end="3866"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction</span></code></pre></div></div></div></div></div></div></div></div></div></div></div></div></div></pre>

# 1. Encapsulation

Encapsulation means **bundling data and methods together** and controlling access to the data.

Public Attribute

Protected Attribute (_)

Private Attribute (__)

# 2. Inheritance

A child class inherits from a parent class.

class Animal:

def speak(self):
print("Animal speaks")
class Dog(Animal):
pass

dog = Dog()

dog.speak()


| Feature               | Method Overloading                         | Method Overriding                                                    |
| --------------------- | ------------------------------------------ | -------------------------------------------------------------------- |
| Definition            | Same method name with different parameters | Child class provides its own implementation of a parent class method |
| Supported in Python?  | ❌ Not directly                            | ✅ Yes                                                               |
| Inheritance Required? | No                                         | Yes                                                                  |
| Purpose               | Handle different types/number of arguments | Change parent behavior in child class                                |
| Runtime Decision      | Based on arguments (other languages)       | Based on object type                                                 |

# `super()`

Call the parent class constructor or methods.

# 1. Single Inheritance

One parent and one child.

<pre class="overflow-visible! px-0!" data-start="4487" data-end="4511"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>Animal
   |
 Dog</span></code></pre></div></div></div></div></div></div></div></div></div></div></div></div></div></pre>

# 3. Multilevel Inheritance

<pre class="overflow-visible! px-0!" data-start="5129" data-end="5181"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>Grandparent

      |

Parent

      |

Child</span></code></pre></div></div></div></div></div></div></div></div></div></div></div></div></div></pre>

4. Hierarchical Inheritance

   All children share the same parent behavior.

Animal

/      |      \

Dog     Cat    Lion

# Advantages of Inheritance

* Code reuse
* Less duplication
* Easier maintenance
* Supports polymorphism
* Better organization of related classes
* Easier to extend existing code


| Concept                 | Description                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| Inheritance             | Child class acquires properties and methods from a parent class. |
| Parent/Base/Super Class | The class being inherited from.                                  |
| Child/Derived/Sub Class | The class that inherits from the parent.                         |
| `super()`               | Calls methods or constructors from the parent class.             |
| MRO                     | The order Python follows to search for methods.                  |
| `isinstance()`          | Checks if an object belongs to a class (or its parent classes).  |
| `issubclass()`          | Checks if one class inherits from another.                       |
| Types                   | Single, Multiple, Multilevel, Hierarchical, Hybrid.              |

# What is Polymorphism?

The word **Polymorphism** comes from two Greek words:

* **Poly** = Many
* **Morph** = Forms

So,

> **Polymorphism means "one interface, many forms."**

The same method, function, or operator can behave differently depending on the object or data it is used with.3

# Types of Polymorphism in Python

Python supports:

1. Duck Typing
2. Method Overriding (Runtime Polymorphism)
3. Operator Overloading
4. Function Polymorphism (Built-in Functions)

# 1. Duck Typing

Duck typing is a core Python concept.

The rule is:

> "If it walks like a duck and quacks like a duck, treat it as a duck."

Python doesn't care about the class.

It only cares whether the object has the required method.

# 2. Runtime Polymorphism (Method Overriding)

This occurs when a child class overrides a parent class method.

# 3. Operator Overloading

Operators also behave differently for different types.


| Feature                | Inheritance                      | Polymorphism                                        |
| ---------------------- | -------------------------------- | --------------------------------------------------- |
| Meaning                | Child class inherits from parent | Same interface behaves differently                  |
| Purpose                | Reuse code                       | Provide different implementations                   |
| Requires Parent Class? | Yes                              | Often, but duck typing can work without inheritance |
| Main Benefit           | Code reuse                       | Flexibility and extensibility                       |

# What is Abstraction?

### Definition

> **Abstraction means hiding the internal implementation details and showing only the essential functionality to the user.**

The user only knows **what** an object does, not **how** it does it.

## Example 3: Mobile Phone

You press:

<pre class="overflow-visible! px-0!" data-start="1030" data-end="1046"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>Call</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

You don't know:

* Which network tower is used
* How packets travel
* How voice is encoded

The complexity is hidden.

# Abstraction in Python

Python provides abstraction using the **`abc` (Abstract Base Class)** module.

The `abc` module lets you create **abstract classes** and **abstract methods**.

# What is an Abstract Class?

An abstract class is a class that:

* Cannot be instantiated (you cannot create its object directly)
* Is meant to be inherited
* Can contain abstract and normal methods

Think of it as a blueprint.

# What is an Abstract Method?

An abstract method:

* Has only a declaration (or a placeholder)
* Has no meaningful implementation
* Must be implemented by every concrete child class

from abc import ABC, abstractmethod

class Parent(ABC):

@abstractmethod
def method_name(self):
pass


| Feature        | Abstraction                        | Encapsulation                             |
| -------------- | ---------------------------------- | ----------------------------------------- |
| Purpose        | Hide implementation details        | Hide data                                 |
| Focus          | What an object does                | Protect how data is accessed              |
| Achieved Using | Abstract classes, abstract methods | Private/protected members, properties     |
| Example        | ATM interface                      | Bank balance stored in a private variable |

            OOP
             │
┌───────────────┼────────────────┐
│               │                │
Encapsulation   Inheritance     Abstraction
│              │
▼              ▼
Method Overriding   Abstract Methods
│              │
└──────┬───────┘
▼
Polymorphism


# Advantages of Abstraction

* Hides unnecessary implementation details.
* Makes code easier to understand and use.
* Encourages consistent interfaces.
* Improves maintainability.
* Supports large, modular applications.




| Concept           | Description                        |
| ----------------- | ---------------------------------- |
| Class             | Blueprint for objects              |
| Object            | Instance of a class                |
| `__init__()`      | Constructor                        |
| `self`            | Current object                     |
| Instance Variable | Unique per object                  |
| Class Variable    | Shared by all objects              |
| Instance Method   | Works with object data             |
| `@staticmethod`   | Independent utility method         |
| `@classmethod`    | Works with class data              |
| Inheritance       | Reuse code from another class      |
| Encapsulation     | Bundle data and behavior           |
| Polymorphism      | Same interface, different behavior |
| Abstraction       | Hide implementation details        |
| `super()`         | Access parent class functionality  |
| Magic Methods     | Customize built-in behavior        |
