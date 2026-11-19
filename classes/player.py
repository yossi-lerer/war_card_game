from classes.display import Display

class Player:
    def __init__(self, player_cards, computer_cards) -> None:
        self.player_cards = player_cards
        self.computer_cards = computer_cards
    
    def make_turn(self):
        player_card = self.player_cards.pop(0)
        computer_card = self.computer_cards.pop(0)
        Display.drawing_card(player_card, computer_card)
        msg = ""
        if player_card[0] > computer_card[0]:
            self.player_cards.append(player_card)
            self.player_cards.append(computer_card)
            msg = "Player won the round!"
        elif player_card[0] < computer_card[0]:
            self.computer_cards.append(player_card)
            self.computer_cards.append(computer_card)
            msg = "computer won the round!"
        else:
            self.player_cards.append(player_card)
            self.computer_cards.append(computer_card)
            msg = "It's a draw!"
        Display.display_round_msg(player_card, computer_card, msg, self.player_cards, self.computer_cards)