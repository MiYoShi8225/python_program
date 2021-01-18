class Sharp:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

class Square(Sharp):
    def area(self):
        return self.width * self.len

a_square = Square(20, 20)
print(a_square.area())
