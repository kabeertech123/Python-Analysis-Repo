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
            self.display_info_player_cards()
            
            if self.player_hand.cards[i].value == 0:
                self.player_chooses_ace_value()
            
        
        
        
    def player_chooses_ace_value(self):
        player_choice = int(input("You have recieved an ace, enter the value u want the ace to be :"))
        
        
        for player_cards in (self.player_hand.cards):
            if player_choice == 1:
                player_cards.value = 1
                
                
            elif player_choice == 11:
                player_cards.value = 11
                

            
    def display_info_player_cards(self):
        for player_card in (self.player_hand.cards):
            print(player_card.display())
          
    
    def display_info_dealer_cards(self):
        for dealer_card in (self.dealer_hand.cards):
            print(dealer_card.display())
            
            

    def calculate_value_dealer(self):
        total = 0
        for i in range (0, len(self.dealer_hand.cards)):
            total += self.dealer_hand.cards[i].value
            
        return total
    
    def game_loop(self):
        loop = True
        
        while loop:
            
            self.deal_initial_cards()
            print('___________________')
            self.display_info_dealer_cards()
            print(self.calculate_value_dealer())
            
           
            
                    
                




        



game = Game()


print('Enter the 1 key if you want to play blackjack')
print('')
print('Or to quit, press the number 2 key')

start_game = int(input('Your choice: '))

if start_game == 2:
    loop = False
    
else:
    game.game_loop()