class Trainer:
    def __init__(self, name, potions, pokemons, active_pokemon):
        self.name = name
        self.potions = potions
        self.pokemons = pokemons
        self.active_pokemon = active_pokemon

    def use_potion(self):
        self.potions -= 1
        print("{0} used a potion on {1}".format(
            self.name, self.pokemons[self.active_pokemon].name))
        self.pokemons[self.active_pokemon].heal()

    def attack_opponent(self, enemy, damage):
        self.pokemons[self.active_pokemon].attack(enemy, damage)

    def switch_pokemon(self, poke_index):
        if poke_index == self.active_pokemon:
            print("{0} is already active!".format(
                self.pokemons[self.active_pokemon].name))
            return
        if self.pokemons[poke_index].is_knocked_out:
            print("Cannot switch to a knocked out pokemon")
            return
        self.active_pokemon = poke_index
        print("{0} switched pokemon to {1}".format(
            self.name, self.pokemons[self.active_pokemon].name))
