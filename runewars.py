from factions import Faction
from unit_types import Bowman, Footman, Knight, SiegeTower, Archer, PegasusRider, Sorceress, Warrior, Sorcerer, Razorwing,Beastman, Hellhound, Dragon, Giant
from fate_deck import FateDeck
from battle import Battle
from players import HumanPlayer, RandomAIPlayer


random_ai_player_1 = RandomAIPlayer()
random_ai_player_2 = RandomAIPlayer()
human_player = HumanPlayer()

# daqan_lords = Faction("Daqan Lords", random_ai_player_1)
daqan_lords = Faction("Daqan Lords", human_player)
latari_elves = Faction("Latari Elves", random_ai_player_2)

daqan_lords.add_unit_type(Bowman(daqan_lords, 10))
daqan_lords.add_unit_type(Knight(daqan_lords, 2))
daqan_lords.add_unit_type(Footman(daqan_lords, 2))
daqan_lords.add_unit_type(Hellhound(daqan_lords, 1))
daqan_lords.add_unit_type(SiegeTower(daqan_lords, 1))

latari_elves.add_unit_type(Archer(latari_elves, 4))
latari_elves.add_unit_type(Razorwing(latari_elves, 1))
latari_elves.add_unit_type(PegasusRider(latari_elves, 1))
latari_elves.add_unit_type(Sorceress(latari_elves, 1))
latari_elves.add_unit_type(Warrior(latari_elves, 1))


print(latari_elves.unit_types[0])

# daqan_lords.unit_types[4].units[0].is_standing = False
# daqan_lords.unit_types[4].units[0].damage_taken = 2
# daqan_lords.unit_types[4].units[0].has_activated= True

# print(daqan_lords.unit_types[4].units[0])

# print(daqan_lords.unit_types[4].units[0].get_line_str())


fate_deck = FateDeck()

battle = Battle(daqan_lords, latari_elves, fate_deck)

battle.resolve_battle()