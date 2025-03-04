
from random import shuffle

class Card:
    suits = ["spades", "hesrts", "diamonds", "clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, other):
        if self.value < other.value:
            return True
        
        if self.value == other:
            if self.suit < other.suit:
                return True
            else:
                return False
        
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        
        if self.value == other:
            if self.suit > other.suit:
                return True
            else:
                return False
        
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("name1:")
        name2 = input("name2:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "このラウンドは {} が勝ちました。"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{}は{}、{}は{}を引きました"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def player_game(self):
        #Deckクラスでシャッフルしたカード達を格納する
        cards = self.deck.cards

        print("##戦争を始めます！")
        
        #カードの枚数が2枚以上(カードは1ループで2回減るので実質0より大きい時)でループする
        while len(cards) >= 2:
            m = "q　で終了、それ以外のキーでPlay:"
            response = input(m)
            #qが入力されたらループから抜ける
            if response == "q":
                break

            #p1cとp2cにdeckのカードをpopしたものを格納する
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()

            #p1nとp2nに名前を格納する
            p1n = self.p1.name
            p2n = self.p2.name

            #drawでp1c,p2cに格納された値を表示する
            self.draw(p1n, p1c,p2n, p2c)

            #p1cとp2cの比較を行って勝敗を決定する
            """この下の比較が上で定義したltやgtで判定を行う"""
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        #ゲーム全体のジャッジを行う
        win = self.winner(self.p1, self.p2)
        print("ゲーム終了です。{}".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            result = p1.name + " の勝利です。"
            return result

        if p1.wins < p2.wins:
            result = p2.name + " の勝利です。"
            return result

        return "引き分けです"

game = Game()
game.player_game()

"""
card1 = Card(10, 2)
card2 = Card(4, 3)

print(card1," : ",card2)

print(card1 > card2)
"""
