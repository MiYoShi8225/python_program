class Reactangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len
    
    def change_size(self, w, l):
        self.width = w
        self.len = l


reactangle = Reactangle(10,20)
print(reactangle.area())

reactangle.change_size(20, 300)
print(reactangle.area())
