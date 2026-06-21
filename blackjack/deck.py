from card import Card

class Deck:
    
        
        
    def create_deck(self):
        self.cards = []
        suit_changer = 0
        counter = 0
        suit_list = ['Spades', 'Hearts', 'Diamond', 'Clubs']
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
        pass
    
    def draw_card(self):
        pass
    
    
    
deck = Deck()
deck.create_deck()
deck.print_deck()
