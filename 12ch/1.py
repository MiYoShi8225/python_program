class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

orl = Orange(10, "dark orange")
print(orl)
print(orl.weight)
orl.weight = 100
print(orl.weight)
print(orl.color)
orl.color = "red"
print(orl.color)
