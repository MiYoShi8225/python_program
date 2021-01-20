import math
#pow は (x, y)とした時にxのy乗の計算結果を返す(今回は8)
print(math.pow(2, 3))

import random
#randint は(x, y)とした時にx~yの値でランダムな値を返す(今回は0~100)
while True:
    if random.randint(0, 100) == 0:
        print(0)
        break

import statistics
num = [1, 5, 33, 12, 46, 33, 2]
print(statistics.mean(num)) #mean　平均値
print(statistics.median(num)) #median 中央値
print(statistics.mode(num)) #mode 最頻値

