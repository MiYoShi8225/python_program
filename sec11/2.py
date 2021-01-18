class Queu:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        #insertはリスト番号まで指定して値を入れる
        self.items.insert(0, item)
    
    def dequeu(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

#print(a_queu.is_empty())

a_queu = Queu()
for i in range(5):
    print("set",i)
    a_queu.enqueue(i)

print(a_queu.items)
while a_queu.size():
    print(a_queu.dequeu())


print(a_queu.size())
