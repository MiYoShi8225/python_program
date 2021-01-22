class Reactangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len
    
    def change_size(self, w, l):
        self.width = w
        self.len = l

reac = Reactangle(20 , 10)
print(reac.area())

reac.change_size(10, 4)
print(reac.area())
