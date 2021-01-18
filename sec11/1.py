class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

num = Stack()

for i in range(0, 6):
    print(i)
    num.push(i)

print(num.items)

while num.size():
    print(num.pop())


"""
for c in "Hello":
    num.push(c)

reverse = ""

while num.size():
    reverse += num.pop()

print(reverse)
"""

