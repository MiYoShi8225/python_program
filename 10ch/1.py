def hangman(word):
    worng = 0
    stage = [
        " 0 ",
        " | ",
        "/|\\",
        " | ",
        " | ",
        "/ \\"
    ]
    answer = list(word)
    dip = ["_"] *len(answer)
    win = False
    print("start.")

    while worng < len(stage)+1:
        print(dip)
        guest = input("文字を予想しよう")

        if len(guest) != 1:
            print("1文字だけ入力")
            continue

        if guest in answer:
            print("\"{}\"は正解です。".format(guest))
            index_num = answer.index(guest)
            dip[index_num] = guest
            answer[index_num] = "XX"
        else:
            print("\"{}\"は不正解です。".format(guest))
            for i in range(0,worng):
                print(stage[i])
            worng += 1
        
        if "_" not in dip:
            print("すべて正解です。\n答えは{}".format(word))
            win = True
            break

    if win == False:
        print("終了です。\n答えは\"{}\"です。".format(word))
        
hangman("test")
