from pokemon import Pokemon
from trainer import Trainer


pok1 = Pokemon("Magikarp", "Water", False)
pok2 = Pokemon("Charmander", "Fire", False)
ash = Trainer("Ash", 3, [pok1, pok2], 0)

pok3 = Pokemon("Bulbasaur", "Grass", False)
pok4 = Pokemon("Squirtle", "Water", False)
misty = Trainer("Misty", 4, [pok3, pok4], 0)

pok1.level_up()
pok2.level_up()
pok3.level_up()
pok4.level_up()
pok1.level_up()
pok2.level_up()
pok3.level_up()
pok4.level_up()
pok1.level_up()
pok2.level_up()
pok3.level_up()
pok4.level_up()

ash.attack_opponent(misty, 2)
misty.attack_opponent(ash, 1)
ash.switch_pokemon(1)
ash.attack_opponent(misty, 3)
misty.switch_pokemon(1)
misty.attack_opponent(ash, 2)
ash.attack_opponent(misty, 1)
ash.switch_pokemon(0)
ash.switch_pokemon(0)
ash.switch_pokemon(1)
