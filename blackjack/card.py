class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        

    
    def display(self):
       return [

            "┌─────────┐",

            f"│{self.value:<2}       │",

            "│         │",

            f"│    {self.suit}    │",

            "│         │",

            f"│       {self.value:>2}│",

            "└─────────┘"

        ]
            