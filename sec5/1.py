class Orange:
    def __init__(self, w ,c):
        self.weight = w
        self.color = c
        print("Created!")

orl = Orange(10, "dark orange")
#orl = Orange() ←バグる
orl.weight = 100
orl.color = "light orange"


print(orl.weight)
print(orl.color)
