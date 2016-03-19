import sys
from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll

class Game():
    def set_up(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        if self.monster.attack():
            print("{} is attacking!".format(self.monster))
            if input("Dodge Y/n :").lower() == 'y':
                if self.player.dodge():
                    print("You avoided the attack!")
                else:
                    print('You got hit!')
                    self.player.hit_points -1
            else:
                print("{} hit you for 1 point".format(self.monster))
                self.player.hit_points -1
        else:
            print("{} isnt attacking this turn".format(self.monster))


    def player_turn(self):
        player_choice = input("[A]ttack, [R]est, [Q]uit: ").lower()
        if player_choice == 'a':
            print('You\'re attacking {}'.format(self.monster))
            if self.player.attack():
                if self.monster.dodge():
                    print("{} dodged your attack".format(self.monster))
                else:
                    if self.player.leveled_up():
                        self.monster.hit_points -=2
                    else:
                        self.monster.hit_points -=1
                    print("You hit {}; with your {}".format(self.monster, self.player.weapon))
            else:
                print("You missed!")
        elif player_choice == 'r':
            self.player.rest()
        elif player_choice == 'q':
            sys.exit()
        else:
            self.player_turn()


    def clean_up(self):
        if self.monster.hit_points <= 0:
            self.player.xp += self.monster.xp
            print('You killed {}!'.format(self.monster))
            self.monster = self.get_next_monster()


    def __init__(self):
        self.set_up()

        while self.player.hit_points and (self.monster or self.monsters):
            print('\n'+'='*20)
            print(self.player)
            self.monster_turn()
            print('-'*20)
            self.player_turn()
            self.clean_up()
            print('\n'+'='*20)
        if self.player.hit_points:
            print('You win!')
        elif self.monsters or self.monster:
            print('You lose :(')
        sys.exit()
Game()
