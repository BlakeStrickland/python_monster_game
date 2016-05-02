import sys
from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll
import os


class Game():
    def set_up(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Goblin(),
            Goblin(),
            Goblin(),
            Goblin(),
            Troll(),
            Troll(),
            Troll(),
            Troll(),
            Dragon()
        ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            pass

    def monster_turn(self):
        try:
            if self.monster.attack():
                print("{} {} is attacking!").format(
                    self.monster.color.title(),
                    self.monster.__class__.__name__)
                if self.player.dodge():
                    print("You avoided the attack!")
                else:
                    print('You could not avoid the hit!')
                    if self.monster.__class__.__name__ == 'Dragon':
                        self.player.hit_points -= 2
                    else:
                        self.player.hit_points -= 1

            else:
                print("{} {}'s attack missed!'".format(
                    self.monster.color.title(),
                    self.monster.__class__.__name__))
        except AttributeError:
            print("You have slayed all the beasts!")

    def player_turn(self):
        player_choice = input("[A]ttack, [R]est, [Q]uit: ").lower()
        print('\n')
        if player_choice == 'a':
            print('You\'re attacking {} {}'.format(
                self.monster.color, self.monster.__class__.__name__))
            if self.player.attack():
                if self.monster.dodge():
                    print("{} dodged your attack".format(self.monster))
                else:
                    if self.player.weapon == 'sword':
                        self.monster.hit_points -= 3
                        print("You hit {} {} for {} damage".format(
                            self.monster.color.title(),
                            self.monster.__class__.__name__, 2))
                    elif self.player.weapon == 'bow':
                        self.monster.hit_points -= 5
                        print("You hit {} {} for {} damage".format(
                            self.monster.color.title(),
                            self.monster.__class__.__name__, 2))
                    else:
                        self.monster.hit_points -= 1
                        print("You hit {} {} for {} damage".format(
                            self.monster.color.title(),
                            self.monster.__class__.__name__, 1))
            else:
                print("You missed!")
        elif player_choice == 'r':
            self.player.rest()
        elif player_choice == 'q':
            sys.exit()
        else:
            self.player_turn()

    def print_kills_and_experience(self):
        print('\n' + '**  --  **')
        print('You killed {} {}!'.format(
            self.monster.color.title(), self.monster.__class__.__name__))
        print('You gained {} xp!'.format(self.monster.xp))
        print('**  --  **' + '\n')

    def clean_up(self):
        if self.monster.hit_points <= 0:
            self.player.xp += self.monster.xp
            if self.player.xp > 15:
                self.player.hit_points += 5
                self.player.hit_points = self.player.base_hit_points
            self.print_kills_and_experience()
            self.monster = self.get_next_monster()
            if self.monster is not None:
                print('Wild {} has appeared!'.format(self.monster))

    def print_start(self):
        print('\n'+'='*20)
        print(self.player)
        print(self.monster)
        print('-'*20)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __init__(self):
        self.set_up()
        while self.player.hit_points > 0 and (self.monster or self.monsters):
            self.print_start()
            self.player_turn()
            self.clear_screen()
            self.clean_up()
            self.monster_turn()
        if self.monsters or self.monster:
            print('You have been defeated')
        sys.exit()
Game()
