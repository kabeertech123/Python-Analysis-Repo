from deck import Deck
from card import Card
from hand import Hand
import os

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
            
    
            
           
                
            self.dealer_checks_ace()
        
    def dealer_checks_ace(self):
        for index,  dealer_card in enumerate(self.dealer_hand.cards):
            if dealer_card.value == 0:
                self.dealer_chooses_ace_value(self.calculate_value_dealer(), index)        
            
    def dealer_chooses_ace_value(self, dealer_total, ace_pos):
         
      
        if dealer_total > 19:
            self.dealer_hand.cards[ace_pos].value = 1 
            print("The dealer has set and Ace value to be 1")
         
            
        elif dealer_total > 1:
            self.dealer_hand.cards[ace_pos].value = 11     
            print("The dealer has set and Ace value to be 11")
            
        
        
        
    def player_chooses_ace_value(self):
        player_choice = int(input("You have recieved an ace, enter the value u want the ace to be :"))
        
    
            
    
        for player_cards in (self.player_hand.cards):
            if player_choice == 1 and player_cards.value == 0:
                player_cards.value = 1
                
                
            elif player_choice == 11 and player_cards.value == 0:
                player_cards.value = 11
      
         

            
    def display_info_player_cards(self):
        card_displays = []

        for card in self.player_hand.cards:

            card_displays.append(card.display())

        for line in range(7):

            for card in card_displays:

                print(card[line], end="  ")

            print()
          
    
    def display_info_dealer_cards(self):
        card_displays = []

        for card in self.dealer_hand.cards:

            card_displays.append(card.display())

        for line in range(7):

            for card in card_displays:

                print(card[line], end="  ")

            print()
            
            

    def calculate_value_dealer(self):
        total = 0
        
        for i in range (0, len(self.dealer_hand.cards)):
            total += self.dealer_hand.cards[i].value
            
            
        return total
    
    def calculate_value_player(self):
        total = 0
        
        for i in range (0, len(self.player_hand.cards)):
            total += self.player_hand.cards[i].value
            
            
        return total
    
    def dealer_logic(self, total):
        
        if total > 17:
            print('')
            print(f"Dealer Move: Stand")
            return 'stand'
        elif total > -1 :
            
            card = self.deck.draw_1_card() 
            
            self.dealer_hand.cards.append(card)
            self.dealer_checks_ace()
        
            print('')
            print(f"Dealer Move: Hit")
            
            return 'hit'
            
    def player_logic(self, player_total):
        player_total = self.calculate_value_player()
        for i in range (0, len(self.player_hand.cards)):
            if self.player_hand.cards[i].value == 0:
                self.player_chooses_ace_value()
                
            
            if player_total > 21:
                "You lost "
                print('Player')
                print('-------------------------')
                self.display_info_player_cards()
                
                print(f'Your Total: {player_total}')
                
                
                    
                
                print('Dealer')
                print('-------------------------')
            
                
                self.display_info_dealer_cards()
                
                print('-------------------------')
                
                print(f"Dealer's Total: {self.calculate_value_dealer()}")
                quit()
            
            print('Player')
            print('-------------------------')
            self.display_info_player_cards()
            
            print(f'Your Total: {player_total}')
            
            
                
            
            print('Dealer')
            print('-------------------------')
        
            
            self.display_info_dealer_cards()
            
            print('-------------------------')
            
            print(f"Dealer's Total: {self.calculate_value_dealer()}")
    
        print(f'Your total is: {player_total}')
        
        print('1. Hit')
        print('2. Stand')
        
        player_input = int(input(('Choice: ')))
        
        if player_input == 1:
            
            self.player_hand.cards.append(self.deck.draw_1_card())
            
            
            return player_input
            
            
            
        elif player_input == 2:
            print('you have now performed a stand')
            return player_input
            
    def check_winner (self, player_total, dealer_total, player_input, dealer_input):
        
      
        
        if player_total == 21:
            print("YOU HAVE WONNN")
            print('')
            print('Player')
            print('-------------------------')
            self.display_info_player_cards()
            
            print(f'Your Total: {self.calculate_value_player()}')
            
            print('Dealer')
            print('-------------------------')
        
            
            self.display_info_dealer_cards()
            
            print('-------------------------')
            
            print(f"Dealer's Total: {self.calculate_value_dealer()}")
            
            return False
            
        elif player_total > 21:
            print('you have lost')
            print('')
            print('Player')
            print('-------------------------')
            self.display_info_player_cards()
            
            print(f'Your Total: {self.calculate_value_player()}')
            
            print('Dealer')
            print('-------------------------')
        
            
            self.display_info_dealer_cards()
            
            print('-------------------------')
            
            print(f"Dealer's Total: {self.calculate_value_dealer()}")
    
            
            return False
        
        elif dealer_total == 21:
            print('you have lost')
            print('')
            print('Player')
            print('-------------------------')
            self.display_info_player_cards()
            
            print(f'Your Total: {self.calculate_value_player()}')
            
            print('Dealer')
            print('-------------------------')
        
            
            self.display_info_dealer_cards()
            
            print('-------------------------')
            
            print(f"Dealer's Total: {self.calculate_value_dealer()}")
            
            return False
        
        elif dealer_total > 21:
            print('you have wonnn')
            print('')
            print('Player')
            print('-------------------------')
            self.display_info_player_cards()
            
            print(f'Your Total: {self.calculate_value_player()}')
            
            print('Dealer')
            print('-------------------------')
        
            
            self.display_info_dealer_cards()
            
            print('-------------------------')
            
            print(f"Dealer's Total: {self.calculate_value_dealer()}")
    
            
            return False
        
        elif player_input == 2 and dealer_input == 'stand' and player_total > dealer_total:
            print('You have wonnnn')
            print('')
            print('Player')
            print('-------------------------')
            self.display_info_player_cards()
            
            print(f'Your Total: {self.calculate_value_player()}')
            
            print('Dealer')
            print('-------------------------')
        
            
            self.display_info_dealer_cards()
            
            print('-------------------------')
            
            print(f"Dealer's Total: {self.calculate_value_dealer()}")
    
            return False
            

        elif player_input == 2 and dealer_input == 'stand' and player_total < dealer_total:
            print('You have losttt')
            print('')
            print('Player')
            print('-------------------------')
            self.display_info_player_cards()
            
            print(f'Your Total: {self.calculate_value_player()}')
            
            print('Dealer')
            print('-------------------------')
        
            
            self.display_info_dealer_cards()
            
            print('-------------------------')
            
            print(f"Dealer's Total: {self.calculate_value_dealer()}")
    
            return False
        elif player_input == 2 and dealer_input == 'stand' and player_total == dealer_total:
            print('It is a tie')
            print('')
            print('Player')
            print('-------------------------')
            self.display_info_player_cards()
            
            print(f'Your Total: {self.calculate_value_player()}')
            
            print('Dealer')
            print('-------------------------')
        
            
            self.display_info_dealer_cards()
            
            print('-------------------------')
            
            print(f"Dealer's Total: {self.calculate_value_dealer()}")
    
            return False
    def game_loop(self):
        loop = True
        checker = True
        
        self.deal_initial_cards()
        while loop:
            print('Player')
            print('-------------------------')
            self.display_info_player_cards()
            
            print(f'Your Total: {self.calculate_value_player()}')
            
            print('Dealer')
            print('-------------------------')
        
            
            self.display_info_dealer_cards()
            
            print('-------------------------')
            
            print(f"Dealer's Total: {self.calculate_value_dealer()}")
            
            self.player_logic(self.calculate_value_player())
            
            self.dealer_logic(self.calculate_value_dealer())
            checker = self.check_winner(self.calculate_value_player(), self.calculate_value_dealer(), self.player_logic(self.calculate_value_player()), self.dealer_logic(self.calculate_value_dealer()))
            
            if checker == False:
                loop = False
                
            
            
            
           
        
            
            
           
            
                    
                




        



def clear_screen():
    print("\033[2J\033[H", end="")

game = Game()

print("=" * 35)
print("          ♠ BLACKJACK ♥")
print("=" * 35)

print('Enter the 1 key if you want to play blackjack')
print('')
print('Or to quit, press the number 2 key')

start_game = int(input('Your choice: '))

clear_screen()


if start_game == 2:
    loop = False
    
else:
    game.game_loop()