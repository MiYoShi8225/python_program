class Lion:
    def __init__(self, name):
        self.name = name

    #これを宣言することで print(lion.name) としなくても　return の値を返すことができる
    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)
