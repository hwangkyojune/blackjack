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
#store score of ranks
scores = [min(i,10) for i in range(1,len(ranks)+1)]
score_of_rank = dict(zip(ranks,scores))
score_of_rank["Ace"] = 11
print(score_of_rank)

#function for mixing card
def shuffle_deck():
    random.shuffle(decks)

# Class Player has drawn cards list(cards), score(total_score) attribute and methods deal card, scoring 
class Player:
    #first, player start with two cards
        def __init__(self,name):
            self.name = name
            #player_end is attribute that decide drawning card
            self.player_end = False
            
            self.total_score = 0
            self.cards = []
            self.deal_card()
            self.deal_card()

        #Update scoring whenever dealing card
        def scoring(self):
            #Player_ranks is rank list Player has
            player_ranks = [score.split(' ')[1] for score in self.cards]
            #Total_score is sum of scores matching ranks 
            total_score = sum([score_of_rank[rank] for rank in player_ranks])
            #When Player has Ace and score is higher than 21, subtract 10
            for rank in player_ranks :
                  if total_score < 21 :
                        break
                  if rank == 'Ace':
                        total_score -= 10
                              
            return total_score

        
        #Function draw card
        def deal_card(self):
              self.cards.append(decks.pop(-1))
              self.total_score = self.scoring()

#playerturn function decide whether continue game
def player_turn(player:Player):
    print('{} hand : {}'.format(player.name, player.cards))
    print('{} score : {}'.format(player.name, player.total_score))
    if player.total_score > 21:
        print('{} bust!'.format(player.name))
        player.player_end = True
    elif player.total_score == 21:
        print('Blackjack!')
        player.player_end = True
    else:
        answer = input('Do you want to hit or stay? ')
        if answer == 'hit':
            print('{} hit!'.format(player.name))
            player.deal_card()
        elif answer == 'stay':
            print('{} stay!'.format(player.name))
            player.player_end = True

#dealer draw cards until score is greater than 17
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
        
#Function printing result
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
        print(f'{player.name} : Lose!')


def play_game():
    shuffle_deck()

    num = int(input('How many people play? '))
    players = []
    for i in range(num):
        player = Player('Player{}'.format(i+1))
        players.append(player)
    dealer = Player('Dealer')
    
    print("Welcome to BlackJack!\n")
    
    while True :
        for player in players:
            if not player.player_end :
                player_turn(player)

        if not dealer.player_end :
            dealer_turn(dealer)

        all_player_end = all(player.player_end for player in players)
        if all_player_end and dealer.player_end:
            break
        print("===============================================================")
    
    # print score of dealer and all players
    print('\nTotal scores of the game')
    for player in players:
        print("{}'s total score : {}".format(player.name, player.total_score))
    print("Dealer's total score :", dealer.total_score)

    print('\nThe result of the game')
    for player in players:
        print_result(dealer, player)
        

play_game()
