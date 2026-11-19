class Display:

    @staticmethod
    def menu():
        print('''
        1. Play turn
        2. Exit
        ''')    
    
    @staticmethod
    def menu_in_exit():
        print('''
        1. New game
        2. Exit
        ''')    

    @staticmethod
    def user_input():
        user_choose = ""
        while not user_choose.isdigit():
            user_choose = (input('''
        Select a number from the menu display: '''))
        return int(user_choose)
    
    @staticmethod
    def display_round_msg(player, computer, msg, player_cards, computer_cards):
        print(f'''
        ========== TURN ==========
        Player: {Display.convert_to_display(player)[0]} {Display.convert_to_display(player)[1]}
        Computer: {Display.convert_to_display(computer)[0]} {Display.convert_to_display(computer)[1]}
        {msg}
        Player cards: {len(player_cards)} | Computer cards: {len(computer_cards)}
        ==========================
        ''')

    @staticmethod
    def convert_to_display(card):
        if card[0] == 11:
            return ("J", card[1])
        if card[0] == 12:
            return ("Q", card[1])
        if card[0] == 13:
            return ("K", card[1])
        if card[0] == 14:
            return ("A", card[1])
        return card

    @staticmethod
    def drawing_card(player_card, Computer_card):
        print(f'''
        Player: {player_card[0]} {player_card[1]}
        Computer: {Computer_card[0]} {Computer_card[1]}
        ''')