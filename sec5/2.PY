class orange:
    def __init__(self, w, c):
        #weightは重さ(g)
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created")

    def rot(self, days, temp):
        #tempは温度
        self.mold = days * temp

orange = orange(200, "orange")
print(orange.mold)

orange.rot(10, 37)
print(orange.mold)

