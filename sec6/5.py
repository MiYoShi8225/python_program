class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("stanley", "Bulldog", mick)

#mickで作成したオブジェクトをstanに反映した時に stan→owner→nameで情報が格納されている
print(stan.owner)
print(stan.owner.name)


