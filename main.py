from classes.card import Card
from classes.game_manager import GameManager
from classes.display import Display
from classes.player import player

class Game:
    def __init__(self, GameManager, Card) -> None:
        self.GameManager = GameManager
        self.Card = Card

    
    def configuration(self):
        card = self.Card()
        card.create_deck()
        card.shuffling_cards()
        dealing_cards = card.dealing_cards()
        GameManager = self.GameManager(player("player", dealing_cards[0]), player("computer", dealing_cards[1]))
        return GameManager
    
    def durning_game(self, GameManager):
        while True:
            Display.menu()
            user_choose = Display.user_input() 
            if user_choose == 1:
                GameManager.make_turn()
            if user_choose == 2:
                Display.menu_in_exit()
                user_choose_menu_in_exit = Display.user_input()
                if user_choose_menu_in_exit == 1:
                    GameManager = self.configuration()
                    GameManager.make_turn()
                elif user_choose_menu_in_exit == 2:
                    break

    def run(self):
        GameManager = self.configuration()
        self.durning_game(GameManager)

if __name__ == "__main__":
    game = Game(GameManager, Card).run()