from classes.card import Card
from classes.player import Player

class Game:
    def __init__(self, Player, Card) -> None:
        self.Player = Player
        self.Card = Card

    def display_game(self):
        print('''
        1. Play turn
        2. Exit
        ''')    
    
    def run(self):
        card = self.Card()
        card.create_deck()
        card.shuffling_cards()
        dealing_cards = card.dealing_cards()
        player = self.Player(dealing_cards[0], dealing_cards[1])
        while True:
            self.display_game()
            user_choose = int(input("        enter your choose "))
            if user_choose == 1:
                player.make_turn()
            if user_choose == 2:
                break


game = Game(Player, Card)
game.run()