class Person:
    def __init__(self):
        self.name = "Bob"

bob = Person()
same_bob = bob


print("bob is same_bob:",bob is same_bob)

another_bob = Person()
print("bob is another_bob:",bob is another_bob)

print("bob:",bob)
print("same_bob:",same_bob)
print("another_bob:",another_bob)
