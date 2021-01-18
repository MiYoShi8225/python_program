class Sharp:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

class Square(Sharp):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))

a_square = Square(20, 25)
print(a_square.area())
a_square.print_size()


