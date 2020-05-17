from advantage import advantage
from disadvantage import disadvantage


class Pokemon:
    def __init__(self, name, _type, is_knocked_out):
        self.name = name
        self.level = 1
        self._type = _type
        self.max_health = self.level
        self.is_knocked_out = is_knocked_out
        self.current_health = self.level
        self.exp = 0

    def lose_health(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
        print("{0} now has {1} hp ".format(self.name, self.current_health))
        if self.current_health == 0:

            self.knock_out()

    def gain_exp(self, enemy):
        diff = enemy.pokemons[enemy.active_pokemon].level - self.level
        diff = 1 if diff <= 0 else diff
        self.exp += 5 * diff
        if self.exp == self.level * 10:
            self.level_up()

    def knock_out(self):
        self.is_knocked_out = True
        print("{0} was knocked out".format(self.name))

    def revive(self):
        self.is_knocked_out = False
        self.current_health = 1
        print("{0} has been revived".format(self.name))

    def heal(self):
        if self.is_knocked_out == True:
            self.revive()
        self.current_health = self.max_health
        print("{0} now has {1} hp ".format(self.name, self.current_health))

    def level_up(self):
        self.level += 1
        self.max_health = self.level
        self.current_health = self.max_health
        print("{0} just leveled up! {1} is now level {2}!".format(
            self.name, self.name, self.level))

    def attack(self, enemy, damage):
        if self.is_knocked_out:
            print(
                "{0} is knocked out and cannot attack! Switch pokemon first.".format(self.name))
            return
        else:
            print("{0} is attacking {1}'s {2}".format(
                self.name, enemy.name, enemy.pokemons[enemy.active_pokemon].name))
        if advantage(self, enemy.pokemons[enemy.active_pokemon]):
            damage = damage * 2
        if disadvantage(self, enemy.pokemons[enemy.active_pokemon]):
            damage = damage / 2
        print("{0} did {1} damage".format(self.name, damage))
        enemy.pokemons[enemy.active_pokemon].lose_health(damage)

        if enemy.pokemons[enemy.active_pokemon].is_knocked_out:
            self.gain_exp(enemy)
