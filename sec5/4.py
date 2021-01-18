from math import pi


class Apple:
    def __init__(self, c, w, f, s):
        self.color = c
        self.weight = w
        self.ffrom = f
        self.sweet = s

base_apple = Apple("red", 200, "aomori", 3)
print(base_apple.color,base_apple.weight,base_apple.ffrom,base_apple.sweet)

class Circle:
    import math
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r**2*pi

circle = Circle(3)

print(circle.area())

class Triangle:
    def __init__(self, l, h):
        self.len = l
        self.high =h
    def area(self):
        return self.len*self.high/2

triangle = Triangle(4, 5)
print(triangle.area())



