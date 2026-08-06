# Single inheritance
# One parent and one child.

class A:

    def demo(self):
        print("Hi")

class B(A):

    def demo1(self):
        print("bye")

b = B()
b.demo1()
b.demo()