from classes.card import Card
from classes.display import Display
from classes.player import Player
import random

class Game:
    def __init__(self) -> None:
        self.first_player = Player
        self.second_player = Player
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

    def make_turn(self):
        first_player = self.first_player.cards.pop(0) # type: ignore
        second_player = self.second_player.cards.pop(0) # type: ignore
        Display.drawing_card(first_player, second_player, self.first_player, self.second_player)
        msg = ""
        if first_player.num > second_player.num:
            self.first_player.cards.append(first_player) # type: ignore
            self.first_player.cards.append(second_player) # type: ignore
            msg = f"{self.first_player.name} won the round!" # type: ignore
        elif first_player.num < second_player.num:
            self.second_player.cards.append(first_player) # type: ignore
            self.second_player.cards.append(second_player) # type: ignore
            msg = f"{self.second_player.name} won the round!" # type: ignore
        else:
            self.first_player.cards.append(first_player) # type: ignore
            self.second_player.cards.append(second_player) # type: ignore
            msg = "It's a draw!"
        Display.display_round_msg(first_player, second_player, msg, self.first_player, self.second_player)

    def configuration(self):
        self.deck = []
        self.create_deck()
        self.shuffling_cards()
        dealing_cards = self.dealing_cards()
        self.first_player = Player("player", dealing_cards[0])
        self.second_player = Player("computer", dealing_cards[1])
    
    def durning_game(self):
        while True:
            Display.menu()
            user_choose = Display.user_input() 
            if user_choose == 1:
                self.make_turn()
            if user_choose == 2:
                Display.menu_in_exit()
                user_choose_menu_in_exit = Display.user_input()
                if user_choose_menu_in_exit == 1:
                    self.configuration()
                elif user_choose_menu_in_exit == 2:
                    break

    def run(self):
        self.configuration()
        self.durning_game()
