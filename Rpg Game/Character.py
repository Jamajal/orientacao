
import random
from .Combat import Combat

class Character(Combat):
    def __init__(self, name: str, health: int, min_attack: int, max_attack: int, defence: int):
        self.name = name
        self.max_health = health
        self.current_health = health
        self.min_attack = min_attack
        self.max_attack = max_attack
        self.defence = defence
        self.can_special_move = False
        self.special_move_type = None
        self.special_move_power = 0
        self.weapon_name = None
        self.weapon_force = 0
        self.heal_potions = 0

    def make_attack(self):
        attack_power = random.randint(self.min_attack, self.max_attack)
        return attack_power + self.weapon_force

    def special_move(self):
        if self.can_special_move:
            if self.special_move_type == 'heal':
                self.current_health += self.special_move_power
                self.check_health()

            elif self.special_move_type == 'attack':
                return self.special_move_power
            
            else:
                print('Algo deu errado com seu poder especial!')

        else:
            print('Você ainda não aprendeu nenhum poder especial!')

    def learn_special_move(self, type: str, power: int) -> None:
        self.special_move_type = type
        self.special_move_power = power

    def check_weapon(self, weapon: str, force: int) -> None:
        if weapon != None:
            print(f'Você adquiriu {weapon}!')
            self.weapon_name = weapon
            self.weapon_force = force
        else:
            print(f'Perdeu a {self.weapon_name}!')
            self.weapon_name = None
            self.weapon_force = 0

    def heal_self(self):
        if(self.heal_potions > 0):
            self.current_health += 50
            self.check_health()
            self.heal_potions -= 1
        else:
            print('Você não possui mais poções de cura!')

    def check_health(self):
        if self.current_health > self.max_health:
            self.current_health = self.max_health
            return True

        elif self.current_health <= 0:
            return self.die()
        
    def take_damage(self, damage):
        damage_taken = damage - self.defence

        if damage_taken > 0:
            print(f'Você sofre {damage_taken} pontos de vida!')
            self.current_health -= damage_taken
            self.check_health()

        else:
            print(f'O ataque não foi suficiente para te ferir!')

    def die():
        print('Você morreu... Game over!')
        return False