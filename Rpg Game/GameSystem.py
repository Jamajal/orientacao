from .Enemy import Enemy

class GameSystem:
    def __init__(self, mode):
        if mode == 'facil':
            self.fights = 2

        elif mode == 'medio':
            self.fights = 4

        else:
            self.fights = 6

        self.beaten_enemies = 0

    def generate_enemy(self):
        pass

    def player_move_choices(self):
        pass

    def enemy_defeated(self):
        self.beaten_enemies += 1
        self.check_victory()

    def check_victory(self) -> bool:
        if self.beaten_enemies == self.fights:
            print('Você venceu!')
            return True
        
        return False
        
    