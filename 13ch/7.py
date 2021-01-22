class Sharp:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

#小クラスの作成には　Class名(親Class名)　で作成できる
class Square(Sharp):
    def area(self):
        return self.width * self.len

    #↓親クラスにも定義されている関数を再度定義し直すことができる！
    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))


my_sharp = Sharp(20, 35)
my_sharp.print_size()

my_sharp2 = Square(20, 35)
my_sharp2.print_size()
print(my_sharp2.area())
