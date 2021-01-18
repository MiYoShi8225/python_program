import time
import random


class Queu:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        #insertはリスト番号まで指定して値を入れる(今回は0を指定する)
        self.items.insert(0, item)
    
    def dequeu(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def simulate_line(till_show, max_time):
    pq = Queu()
    tix_sold = []

    #人間を100人用意する
    for i in range(100):
        pq.enqueue("person" + str(i))

    #終了時刻を入れて、till_showに入れた秒数だけ加算したものをエンドタイムとする
    t_end = time.time() + till_show
    now = time.time()

    #今の時間がエンドタイム未満であること、そしてpq(人間)がいなくなっていないこと
    while now < t_end and not pq.is_empty():
        now = time.time()

        #ランダムにスリープする時間を設定する
        r = random.randint(0, max_time)
        time.sleep(r)

        #人間の情報を代入
        person = pq.dequeu()
        print(person)

        #チケットを売ることのできた人間をリストで格納
        tix_sold.append(person)
    
    return tix_sold


sold = simulate_line(7, 2)
print(sold)

