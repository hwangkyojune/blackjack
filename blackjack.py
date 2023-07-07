import random

#deck init
decks = []
shapes = ['Hearts','Diamonds','Clubs','Spades']
ranks = ['Ace'] + [str(rank) for rank in range(2,10)] + ['Jack','Queen','King']

for shape in shapes:
    for rank in ranks:
        decks.append(f"{shape} {rank}")
        
len(decks)


#score setting
#뽑은 rank마다의 점수를 저장
scores = [min(i,10) for i in range(1,len(ranks)+1)]
score_of_rank = dict(zip(ranks,scores))


#카드 섞기
def shuffle_deck():
    random.shuffle(decks)

# player class는 소유한 카드 리스트(cards), 점수(total_score) 속성과 카드 뽑기 함수가 있음
class player:
    #각 player마다 total_score 2장부터 시작
        def __init__(self):
            self.cards = []
            self.deal_card(decks)
            self.deal_card(decks)
            self.total_score = self.scoring(self.cards)

        #가지고 있는 카드의 점수 합 반환
        def scoring(self,scores):
              pass
        
        #카드 뽑기 & 카드 소유, 총 점수 업데이트
        def deal_card(self,decks):
              self.cards.append(decks.pop(-1))
              self.total_score = self.scoring(self.cards)

def player1_turn():
    pass



def dealer_turn():
    pass


def play_game():
    print("Welcome to BlackJack!")
    shuffle_deck()

    player1 = player()
    dealer = player()

    player1_turn(player1)
    dealer_turn(dealer)

play_game()
