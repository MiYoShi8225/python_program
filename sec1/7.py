"""
name = "The"
for chara in name:
    print(chara)

a = "test"
if("t" in a):
    print(a)
else:
    print("X")

"""
"""
tv = ["GOT", "NARCOS", "VICE"]
i = 0
for show in tv:
    print(show)

    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)


#upper はすべての文字を大文字にする
tv = ["GOT", "NARCOS", "VICE"]
coms = ["Arrested Development","friends","Always Sunny"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)


for i in range(1,11):
    print(i)


x = 10
while x > 0:
    print("{}".format(x))
    x -= 1

print("happy new yaer!")


for i in range(1,100):
    print(i)
    if(i == 24):
        break


qs = [
    "what is your name?",
    "what is your fav. color?",
    "what is your quest?"
    ]

n = 0

while True:
    print("Type q to quit")
    a = input(qs[n])
    if(a == "q"):
        break
    n = (n+1)%3


for i in range(1,3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []

for i in list1:
    for j in list2:
        added.append(i + j)
        print(added)


while input("y or n:") == "y":
    for i in range(1,6):
        print(i)


for i in range(25,51):
    print(i)


list = [2,3,5,7,11,13,17,19,23]

while True:
    try:
        a = input("number or 'q':")
        if a == "q":
            print("end")
            break
        a = int(a)

        if a in list:
            print("OK")
        else:
            print("NG")
    except Exception as e:
        print("Error")    


list1 = [8,19,148,4]
list2 = [9,1,33,83]
list3 = []

for i in list1:
    for j in list2:
        a = i * j
        list3.append(a)

print(list3)
"""


