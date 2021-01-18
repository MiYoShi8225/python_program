"""
#リスト型:[]　配列のように文字や数を入れることができる
random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")
print(random)
print(random)

print(len(random))

a = list("A")
a.append("B")
print(a)

my_tuple = tuple()
print(my_tuple)
my_tuple = ()
print(my_tuple)
"""
"""
#タプル型:()　リスト型と異なり一度入れた文字や数は変更することができない
rndm = ("M.Jackson", 1985, True)
print(rndm)

dya = ("1983", "Brave New World", "test")
print(dya[0])
#dya[0] = "test" ←エラーになる

print("test" in dya)
"""

"""
#辞書型:{}　リスト型と異なり「辞書名：キー」の組み合わせでできている
my_dict = {}
print(my_dict)

fruit = {"Apple": "red", "Banana": "Yellow"}
print(fruit)
print(fruit["Apple"])
"""
"""
songs = {"1":"fun","2":"blue","3":"me"}

n = input("number:")
if(n in songs):
    song = songs[n]
    print(song)
else:
    print("none")
"""

"""
lists = []
rap = ["test1","test2","test3"]
rook = ["test4","test5","test6"]
djs = ["test7","test8","test9"]

lists.append(rap)
lists.append(rook)
lists.append(djs)
lists.append("rap")

print(lists)
"""


