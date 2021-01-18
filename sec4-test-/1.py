def hangman(word):
    wrong = 0
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
    #rlettersにwordの文字をリストで入れている
    rletters = list(word)

    #wordの文字数分_(アンダーバー)をboardに導入する
    board = ["_"] * len(word)

    #winにboolean型を入れておく
    win = False
    print("ハングマンへようこそ")

    #ステージ(ハングマン)のリスト数よりもwrong数が小さいのであればループする
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字予想する。"
        char = input(msg)

        #rlettersのリストの中に今回入力した文字があるかを判別する
        if char in rletters:
            #cindにはrlettersのリストの何番目配列なのかを代入する
            cind = rletters.index(char)

            #board(もともと_が入っていたリスト)に今回入力した文字を代入する。
            board[cind] = char

            #rlettersに入っていた文字の部分に$を入れる
            #理由としては同じ文字を含む場合に重複して処理してしまうため
            rletters[cind] = "$"
        
        #上記のif文に対応していないのであれば以下の処理
        else:
            wrong += 1

        #boardに格納されている文字を表示する。
        print(" ".join(board))

        #現在間違えている分のハングマンを表示するための変数(+1はスタート地点)
        e = wrong + 1
        #現在間違えている分のハングマンを表示する
        #joinは表示printで表示する言葉の前にjoinで書かれた言葉を表示する
        print("test\n".join(stages[0:e]))

        #boardの中に_がなくなれば勝ちになる
        if "_" not in board:
            print("あなたの勝ちです。")
            print(" ".join(board))
            win = True
            break

    #winがFalseであれば表示する
    if not win:
        print("\n".join(stages[0:wrong+1]))

        #formatは{}に対して文字を代入する
        print("あなたの負けです。正解は {} {}".format(word, "ppp"))

hangman("cata")
