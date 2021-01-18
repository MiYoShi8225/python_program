class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(10)
y = AlwaysPositive(-20)
z = AlwaysPositive(-40)

print(x + y)

#↓はエラーになる　3つは当然無理
#print(y + y + z)

print(z + y)
