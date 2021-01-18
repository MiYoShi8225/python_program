class Rectangle:
    #クラス変数
    recs = []

    def __init__(self, w, l):
        self.weight = w
        self.len = l
        #self.recs.append([self.weight, self.len])
        self.recs.append((self.weight, self.len))

    def print_size(self):
        print("{} by {}".format(self.weight, self.len))

rect1 = Rectangle(3, 4)
print(Rectangle.recs)

rect2 = Rectangle(5, 6)
print(Rectangle.recs)

rect3 = Rectangle(7, 8)
print(Rectangle.recs)

rect1.print_size()
rect2.print_size()
rect3.print_size()

