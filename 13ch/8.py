class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    
class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "bulldog", mick)
print(stan.owner)

print("name →",stan.owner.name)
print(stan.name, stan.breed)
