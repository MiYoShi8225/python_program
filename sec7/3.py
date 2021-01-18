class Lion:
    def __init__(self, name):
        self.name = name

lion = Lion("Rion")
print(lion)

class Lion2:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

lion = Lion2("Rion")
print(lion)
