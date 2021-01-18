a = int(input("number1:"))
b = int(input("number2:"))
c = int(input("number3:"))

sum = a + b +c

if(sum < 10):
    print("10未満")
else:
    print("10以上")

if(sum <= 10):
    print("10以下")
elif(10 < sum <= 25):
    print("10より大きく25以下")
elif(25 < sum):
    print("25より大きい")

print(a%b)
print((a-a%b)/b)
