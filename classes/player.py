class Player:
    def __init__(self, player_cards, computer_cards) -> None:
        self.player_cards = player_cards
        self.computer_cards = computer_cards
    
    def display_round_msg(self, player, computer, msg):
        print(f'''
        • ========== TURN ==========
        • Player: {self.convert_to_display(player)[0]} {self.convert_to_display(player)[1]}
        • Computer: {self.convert_to_display(computer)[0]} {self.convert_to_display(computer)[1]}
        • {msg}
        • Player cards: {len(self.player_cards)} | Computer cards: {len(self.computer_cards)}
        • ==========================
        ''')

    def convert_to_display(self, card):
        if card[0] == 11:
            return ("J", card[1])
        if card[0] == 12:
            return ("Q", card[1])
        if card[0] == 13:
            return ("K", card[1])
        if card[0] == 14:
            return ("A", card[1])
        return card
   
    def make_turn(self):
        player_card = self.player_cards.pop(0)
        computer_card = self.computer_cards.pop(0)
        print(f"        Player: {self.convert_to_display(player_card)[0]} {self.convert_to_display(player_card)[1]}")
        print(f"        Computer: {self.convert_to_display(computer_card)[0]} {self.convert_to_display(computer_card)[1]}")
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
        self.display_round_msg(player_card, computer_card, msg)