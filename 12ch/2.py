class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mode = 0
        print("created!")
    
    def rot(self, days, tmp):
        self.mod = days * tmp

orl = Orange(10 , "dark orange")
print(orl.weight, orl.color)

orl.rot(10, 20)
print(orl.mod)