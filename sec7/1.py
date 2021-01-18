class Rectangle:
    def __init__(self, w, l):
        self.weight = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.weight, self.len))

my_rectangle = Rectangle(4, 5)
my_rectangle.print_size()
