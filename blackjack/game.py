from deck import Deck
from card import Card
from hand import Hand

class Game:
    
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        
        




    
    def deal_initial_cards(self):
        self.deck.create_deck()
        self.deck.shuffle()
        
        player_inital_cards = self.deck.draw_2_cards()
        dealer_inital_cards = self.deck.draw_2_cards()
    
        
        for i in range (0,2):
            self.player_hand.cards.append(player_inital_cards[i]) 
            self.dealer_hand.cards.append(dealer_inital_cards[i])
            
            if self.player_hand.cards[i] == 0:
                self.player_chooses_ace_value()
            
        
        
        
    def player_chooses_ace_value(self):
        player_choice = int(input("You have recieved an ace, enter the value u want the ace to be :"))
        
        if player_choice == 1:
            for player_cards in (self.player_hand.cards):
                if player_cards.value == 0:
                    player_cards.value = 1
                    
                else:
                    player_cards.value = 11
        
        
            
    
            
    def display_info_player_cards(self):
        for player_card in (self.player_hand.cards):
            print(player_card.display())
          
            
            
            

    
    def game_loop(self):
       
        self.deal_initial_cards()
        self.display_info_player_cards()
           
                
            




    def calculate_value():
            pass
        

loop = True

game = Game()


print('Enter the 1 key if you want to play blackjack')
print('')
print('Or to quit, press the number 2 key')

start_game = int(input('Your choice: '))

if start_game == 2:
    loop = False
    
else:
    game.game_loop()