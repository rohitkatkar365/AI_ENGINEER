class A:
    def __init__(self):
        print("A Class Constructor Called")

    def show(self):
        print(12)

class B(A):

    def __init__(self):
        super().__init__()
        super().show()
        print("B Class Constructor Called")

b = B()
