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
    def display_round_msg(player, computer, msg, first_player, second_player):
        print(f'''
        ========== TURN ==========
        {first_player.name}: {Display.convert_to_display(player)[0]} {Display.convert_to_display(player)[1]}
        {second_player.name}: {Display.convert_to_display(computer)[0]} {Display.convert_to_display(computer)[1]}
        {msg}
        {first_player.name} cards: {len(first_player.cards)} | {second_player.name} cards: {len(second_player.cards)}
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
    def drawing_card(player_card, Computer_card, first_player, second_player):
        print(f'''
        {first_player.name}: {player_card[0]} {player_card[1]}
        {second_player.name}: {Computer_card[0]} {Computer_card[1]}
        ''')