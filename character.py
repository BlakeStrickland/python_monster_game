import random

from combat import Combat


class Character(Combat):
    attack_limit = 10
    xp = 0
    base_hit_points = 20

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        if self.weapon == 'sword':
            roll += 4
        elif self.weapon == 'axe':
            roll += 5
        elif self.weapon == 'bow':
            roll += 12
        return roll > 4

    def get_weapon(self):
        weapon_choice = input('Weapon > [S]word, [A]xe, or [B]ow: ').lower()

        if weapon_choice in 'sab':
            if weapon_choice == 's':
                return 'sword'
            elif weapon_choice == 'a':
                return 'axe'
            else:
                return 'bow'
        else:
            return self.get_weapon()

    def __init__(self, **kwargs):
        self.name = input('Name > ')
        self.weapon = self.get_weapon()
        self.hit_points = self.base_hit_points
        self.level = 0

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "{}, HP: {}, XP: {}".format(self.name, self.hit_points, self.xp)

    def rest(self):
        if self.hit_points < self.base_hit_points:
            self.hit_points += 1

    def level_up(self):
        if self.xp > 10:
            self.hit_points = self.base_hit_points
            self.level += 1
