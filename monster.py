import random
from combat import Combat

COLORS = ['yellow', 'blue', 'orange', 'green']


class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_xp = 1
    max_xp = 2
    weapon = 'sword'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(
            self.min_hit_points, self.max_hit_points)
        self.xp = random.randint(self.min_xp, self.max_xp)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{} {},  HP: {},  XP:  {}'.format(self.color.title(),
                                                 self.__class__.__name__,
                                                 self.hit_points,
                                                 self.xp)

    def battle_cry(self):
        return self.sound.upper()


class Goblin(Monster):
    max_hit_points = 10
    max_xp = 4
    sound = 'squeek'

    def attack(self):
        # attack_limit = 6
        roll = random.randint(1, self.attack_limit)
        return roll > 2


class Troll(Monster):
    min_hit_points = 15
    max_hit_points = 20
    min_xp = 7
    max_xp = 13
    sound = 'growl'


class Dragon(Monster):
    min_hit_points = 20
    max_hit_points = 35
    min_xp = 20
    max_xp = 100
    sound = 'raaaaaaar'
    dodge_limit = 6
    attack_limit = 6

    def dodge(self):
        roll = random.randint(1, self.dodge_limit)
        return roll > 2

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        return roll > 2
