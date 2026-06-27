from card import Card
import random

class Deck:
    
        
        
    def create_deck(self):
        self.cards = []
        suit_changer = 0
        counter = 0
        suit_list = ['♠', '♥', '♦', '♣']
        value_list = [2,3,4,5,6,7,8,9,10, 10, 10, 10, 0]
        for i in range (0, 52):
    
            if(counter > 12 ):
                suit_changer += 1
                
                counter = 0
                
            self.cards.append(Card(suit_list[suit_changer], value_list[counter])) 
     
            counter += 1
     
    
    def print_deck(self):
        for card_obj in (self.cards):
            print(f'{card_obj.suit} : {card_obj.value}')
            print('')
            print('')
       
           
                  
        
    
    def shuffle(self):
    
        random.shuffle(self.cards)
      
        
        
        
    
    def draw_2_cards(self):
        card1 = self.cards[0]
        card2 = self.cards[1]
        temp_list = []
        
        temp_list.append(card1)
        temp_list.append(card2)
        self.cards.remove(card1)
        self.cards.remove(card2)
            
     
        return temp_list
            
           
    
    def draw_1_card(self):
        
    
        card = (self.cards[0])
        self.cards.remove(self.cards[0])
        
        return card
        
        
       




    
