
lists =[]

test = ["test", "test2", "test3"]
dev = ["dev", "dev2", "dev3"]
hack = ["hack", "hack2", "hack3"]

lists.append(test)
lists.append(dev)
lists.append(hack)

print(lists)
#print(lists[2])

#リストに追加したリストに対して追加を行う
lists[0].append("test4")
print(lists)

#indexで格納されている場所を検索する
print("animas".index("i"))

# 「\」はエスケープ文字
print("彼女は\"そうだね\"といった")

# enumurateではインデックスの文字と配列のの値を取り出せる
enumu = ["miyoshi1", "miyoshi2", "miyoshi3"]
for i, new in enumerate(enumu):
    print("No."+str(i)+" "+new)

