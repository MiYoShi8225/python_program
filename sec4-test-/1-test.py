import random
import string

def hangma(word):
    stages = [
        "",
        "__________      ",
        "|               ",
        "|         |     ",
        "|         O     ",
        "|        /|/    ",
        "|        //     ",
        "|               "
    ]
    worng_cnt = len(stages)
    count = 1
    result = False
    disp = ["_"] * len(word)
    
    print(disp)

    answer = list(word)

    while count < worng_cnt:
        user_answer = input("1文字入力：")
        if user_answer in answer:
            print("正解です")
            leng = answer.index(user_answer)
            disp[leng] = user_answer
            answer[leng] = "XX"
            print(disp)

        else:
            print("間違いです。")
            print(disp)
            count += 1
            for i in range(0,count):
                print(stages[i])
        
        if "_" not in disp:
            result = True
            break

    print("##answer: " + word)
    if result is True:
        print("##CLEAR!##")
    else:
        print("##NOT CLEAR##")
        

def GetRandomStr(num):
    global word
    #digits:数字　ascii_lowercase:小文字英語　ascii_uppercase：大文字英語
    word_data = string.digits + string.ascii_lowercase #+ string.ascii_uppercase
    print(word_data)

    #random choiceは1文字(後ろに格納されているリスト？)を取り出す
    #for i in range(0,num):
    word = "".join([random.choice(word_data)for i in range(num)])
    return word

word = str
num = int(input("Please input number:"))
hangma(GetRandomStr(num))

