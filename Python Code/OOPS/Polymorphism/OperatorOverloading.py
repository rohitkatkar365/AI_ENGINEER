class Points:
    def __init__(self,x):
        self.x = x

    def __add__(self, other):
        return Points(self.x + other.x)

    def __str__(self):
        return str(self.x)

p1 = Points(10)
p2 = Points(20)
print(p1 + p2) 