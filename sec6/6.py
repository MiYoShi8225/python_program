#親クラスを上に記載しないと小クラスに反映されない
class Sharp:
    def what_am_i(self):
        return "I am a sharp."

class Rectangle(Sharp):
    def __init__(self, w, l):
        self.wight = w
        self.len = l

    def calculate_perimeter(self):
        return (self.wight + self.len) * 2

class Square(Sharp):
    def __init__(self, l):
        self.len = l
    
    def calculate_perimeter(self):
        return self.len * 4
    
    def change_size(self, l):
        self.len -= l


rectangle = Rectangle(4, 5)
square = Square(4)

print(rectangle.calculate_perimeter())
print(square.calculate_perimeter())

square.change_size(1)
print(square.calculate_perimeter(),"\n")

class Horse:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

rider = Rider("miyoshi")
horse = Horse("uma", rider)

print(horse.name, horse.owner.name)
