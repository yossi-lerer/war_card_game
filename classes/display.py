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
    def drawing_card(player_card, Computer_card, first_player, second_player):
        print(f'''
        {first_player.name}: {Display.convert_to_display(player_card)[0]} {Display.convert_to_display(player_card)[1]}
        {second_player.name}: {Display.convert_to_display(Computer_card)[0]} {Display.convert_to_display(Computer_card)[1]}
        ''')

    @staticmethod
    def convert_to_display(card):
        if card.num == 11:
            return ("J", card.symbol)
        if card.num == 12:
            return ("Q", card.symbol)
        if card.num == 13:
            return ("K", card.symbol)
        if card.num == 14:
            return ("A", card.symbol)
        return (card.num, card.symbol)
