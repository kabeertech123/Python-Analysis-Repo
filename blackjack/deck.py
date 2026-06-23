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
        rand_num1 = random.randint(0, 51)
        rand_num2 = random.randint(0, 51)
        self.draw_card_list = []
        
        if(rand_num1 == rand_num2):
            self.draw_2_cards()
        
        else:
            self.draw_card_list.append(self.cards[rand_num1])
            self.draw_card_list.append(self.cards[rand_num2])
            self.cards.remove(self.cards[rand_num1])
            self.cards.remove(self.cards[rand_num2])
            
     
        return self.draw_card_list
            
           
    
    def draw_1_card(self):
        rand_num1 = random.randint(0, 51)
    
        self.draw_card_list.append(self.cards[rand_num1])
        
        
       




    
