#タプル型
mytuple = tuple()
print(mytuple)

#tupleはリスト内の変更ができなくなるので注意！

rndm = ("M.Jackson", 1985, True)
print(rndm)

"""
rndm[0] = "miyoshi" ←これはエラーになる
理由としては、tuple型は変更が加えられない配列だから
"""

#dict型で辞書型と言われるもので1対1でリストを形成する
dict = dict()
print(dict)

fruit = {"apple":"red","orange":"orange color"}
print(fruit)
print(fruit["apple"])

books = {
    "The trail":"kafka",
    "1984":"Owell",
    "harry":"JK"
}
print(books)
del books["1984"]
print(books)
