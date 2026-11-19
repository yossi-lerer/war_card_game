from classes.display import Display

class GameManager:
    def __init__(self, first_player, second_player) -> None:
        self.first_player = first_player
        self.second_player = second_player
    
    def make_turn(self):
        first_player = self.first_player.cards.pop(0)
        second_player = self.second_player.cards.pop(0)
        Display.drawing_card(first_player, second_player, self.first_player, self.second_player)
        msg = ""
        if first_player.num > second_player.num:
            self.first_player.cards.append(first_player)
            self.first_player.cards.append(second_player)
            msg = f"{self.first_player.name} won the round!"
        elif first_player.num < second_player.num:
            self.second_player.cards.append(first_player)
            self.second_player.cards.append(second_player)
            msg = f"{self.second_player.name} won the round!"
        else:
            self.first_player.cards.append(first_player)
            self.second_player.cards.append(second_player)
            msg = "It's a draw!"
        Display.display_round_msg(first_player, second_player, msg, self.first_player, self.second_player)