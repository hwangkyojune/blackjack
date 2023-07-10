import random

#deck init
decks = []
shapes = ['Hearts','Diamonds','Clubs','Spades']
ranks = ['Ace'] + [str(rank) for rank in range(2,11)] + ['Jack','Queen','King']

for shape in shapes:
    for rank in ranks:
        decks.append(f"{shape} {rank}")
        
len(decks)

#score setting
#뽑은 rank마다의 점수를 저장
scores = [min(i,10) for i in range(1,len(ranks)+1)]
score_of_rank = dict(zip(ranks,scores))
score_of_rank["Ace"] = 11
print(score_of_rank)

#카드 섞기
def shuffle_deck():
    random.shuffle(decks)

# player class는 소유한 카드 리스트(cards), 점수(total_score) 속성과 카드 뽑기 함수가 있음
class Player:
    #각 player마다 total_score 2장부터 시작
        def __init__(self,name):
            self.name = name
            #player_end는 player가 게임을 계속할지 정하는 속성
            self.player_end = False
            
            self.total_score = 0
            self.cards = []
            self.deal_card()
            self.deal_card()
            #self.total_score = self.scoring()

        #가지고 있는 카드의 점수 update
        def scoring(self):
            #player_ranks는 player가 소유하고 있는 각 카드들의 rank 리스트
            player_ranks = [score.split(' ')[1] for score in self.cards]
            #각 rank에 해당하는 score들을 합친 것이 total_score
            total_score = sum([score_of_rank[rank] for rank in player_ranks])
            #Ace가 있고, 21이 넘을 경우 10 제거
            for rank in player_ranks :
                  if total_score < 21 :
                        break
                  if rank == 'Ace':
                        total_score -= 10
                              
            return total_score

        
        #카드 뽑기 & 카드 소유에 추가, 총 점수 업데이트
        def deal_card(self):
              self.cards.append(decks.pop(-1))
              self.total_score = self.scoring()

#playerturn 함수는 게임을 진행할지 멈출지 결정 멈춘다면 Player class의 속성 player_end True변경, 진행한다면 메소드 player.deal_card() 호출
#뽑고 21넘으면 강제종료 & 패배 
def player_turn(player:Player):
    print('Player hand :', player.cards)
    print('Player score :', player.total_score)
    if player.total_score > 21:
        print('Player bust!')
        player.player_end = True
    elif player.total_score == 21:
        print('Blackjack!')
        player.player_end = True
    else:
        answer = input('Do you want to hit or stay? ')
        if answer == 'hit':
            print('Player hit!')
            player.deal_card()
        elif answer == 'stay':
            print('Player stay!')
            player.player_end = True

#딜러턴
#dealer_turn은 점수 17이하면 계속 진행, 21넘으면 dealer 패배
def dealer_turn(dealer:Player):
    print('Dealer hand :', dealer.cards)
    print('Dealer score :', dealer.total_score)
    if dealer.total_score > 21:
        print('Dealer bust!')
        dealer.player_end = True
    elif dealer.total_score >= 17:
        print('Dealer stay!')
        dealer.player_end = True
    else:
        print('Dealer hit!')
        dealer.deal_card()
        
#게임 결과 출력 함수
def print_result(dealer, player):
    if player.total_score < 21:
        if player.total_score > dealer.total_score or dealer.total_score > 21:
            print(f'{player.name} : Win!')
        elif player.total_score == dealer.total_score:
            print(f'{player.name} : Push!')
        else:
            print(f'{player.name} : Lose!')
    elif player.total_score == 21:
        if dealer.total_score == 21:
            print(f'{player.name} : Push!')
        else:
            print(f'{player.name} : Blackjack! Win!')
    else:
        print(f{'{plyaer.name} : Lose!')


def play_game(player : Player ,dealer : Player):
    print("Welcome to BlackJack!")
    
    while True :
        if not player.player_end :
            player_turn(player)

        if not dealer.player_end :
            dealer_turn(dealer)
        
        if player.player_end and dealer.player_end:
            break
        print("===============================================================")
    
    #결과
    print('\nThe result of the game')
    print('Player score :', player.total_score)
    print('Dealer score :', dealer.total_score)
    if player.total_score < 21:
        if player.total_score > dealer.total_score or dealer.total_score > 21:
            print('Player win!')
        elif player.total_score == dealer.total_score:
            print('Push!')
        else:
            print('Player lose!')
    elif player.total_score == 21:
        if dealer.total_score == 21:
            print('Push!')
        else:
            print('Blackjack! Player win!')
    else:
        print('Player lose!')
        
shuffle_deck()

player = Player()
dealer = Player()
play_game(player,dealer)
