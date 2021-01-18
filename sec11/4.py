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

def simulation_tix(time_limit, onetime):
    #リスト作成
    person_list = Queu()
    result_list = []
    #100人人間を代入
    for i in range(100):
        person = "person" + str(i)
        person_list.enqueue(person)

    now = time.time()
    end_time = now + time_limit

    while now < end_time and not person_list.is_empty():
        now = time.time()
        time.sleep(random.randint(0, onetime))

        person = person_list.dequeu()
        print(person)
        result_list.append(person)

    return result_list

result = simulation_tix(10,1)
print(result)
