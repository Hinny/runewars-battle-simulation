from factions import Faction
from units import Bowman, Footman, Knight, SiegeTower, Archer, PegasusRider, Sorceress, Warrior, Sorcerer, Razorwing,Beastman, Hellhound, Dragon, Giant
from fate_deck import FateDeck
from battle_simulator import BattleSimulator

daqan_lords = Faction("Daqan Lords")
latari_elves = Faction("Latari Elves")

daqan_lords.add_unit_type(Bowman(2))
daqan_lords.add_unit_type(Knight(2))
daqan_lords.add_unit_type(Footman(2))
daqan_lords.add_unit_type(Hellhound(1))
daqan_lords.add_unit_type(SiegeTower(1))

latari_elves.add_unit_type(Archer(4))
latari_elves.add_unit_type(Razorwing(1))
latari_elves.add_unit_type(PegasusRider(1))
latari_elves.add_unit_type(Sorceress(1))
latari_elves.add_unit_type(Warrior(1))


fate_deck = FateDeck()

battle_simulator = BattleSimulator(daqan_lords, latari_elves, fate_deck)

battle_simulator.resolve_battle()