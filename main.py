from classes.card import Card
from classes.player import Player
from classes.display import Display

class Game:
    def __init__(self, Player, Card) -> None:
        self.Player = Player
        self.Card = Card
    
    def configuration(self):
        card = self.Card()
        card.create_deck()
        card.shuffling_cards()
        dealing_cards = card.dealing_cards()
        player = self.Player(dealing_cards[0], dealing_cards[1])
        return player
    
    def durning_game(self, player):
        while True:
            Display.menu()
            user_choose = Display.user_input()
            if user_choose == 1:
                player.make_turn()
            if user_choose == 2:
                Display.menu_in_exit()
                user_choose_scend = Display.user_input()
                if user_choose_scend == 1:
                    self.run()
                elif user_choose_scend == 2:
                    break

    def run(self):
        player = self.configuration()
        self.durning_game(player)


game = Game(Player, Card)
game.run()