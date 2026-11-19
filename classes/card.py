import random

class Card:
    def __init__(self) -> None:
        self.deck = []

    def create_deck(self):
        for symbol in ["♥", "♠", "♦", "♣"]:
            for card in range(2,15):
                self.deck.append((card, symbol))
    
    def shuffling_cards(self):
        flag = 0
        while flag < 1000:
            index_one = random.randrange(0, 52)
            index_two = random.randrange(0, 52)
            while index_one == index_two:
                index_two = random.randrange(0, 52)
            store_card = self.deck[index_one]
            self.deck[index_one] = self.deck[index_two]
            self.deck[index_two] = store_card
            flag += 1

    def dealing_cards(self):
        dealing = [[],[]]
        dealing_index = 0
        
        for card in self.deck:
            dealing[dealing_index].append(card)

            if dealing_index == 0:
                dealing_index = 1
            else:
                dealing_index = 0
        
        return dealing