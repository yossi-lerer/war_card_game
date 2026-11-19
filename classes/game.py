from classes.card import Card
from classes.game_manager import GameManager
from classes.display import Display
from classes.player import player
import random

class Game:
    def __init__(self, GameManager) -> None:
        self.GameManager = GameManager
        self.deck = []

    def create_deck(self):
        for symbol in ["♥", "♠", "♦", "♣"]:
            for card in range(2,15):
                self.deck.append(Card(card, symbol))

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

    def configuration(self):
        self.deck = []
        self.create_deck()
        self.shuffling_cards()
        dealing_cards = self.dealing_cards()
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
                elif user_choose_menu_in_exit == 2:
                    break

    def run(self):
        GameManager = self.configuration()
        self.durning_game(GameManager)
