from factions import Faction
from units import Bowman, Footman, Knight, Archer, PegasusRider, Sorcerer, Beastman
from fate_deck import FateDeck
from battle_simulator import BattleSimulator

# Exempel på att skapa lagen och köra en runda av striden
daqan_lords = Faction("Daqan Lords")
latari_elves = Faction("Latari Elves")

# Lägg till enheter i lagen
daqan_lords.add_unit_type(Footman(4))
daqan_lords.add_unit_type(Knight(2))

latari_elves.add_unit_type(Archer(4))
latari_elves.add_unit_type(PegasusRider(1))

fate_deck = FateDeck()

# Skapa instanser av BattleSimulator
battle_simulator = BattleSimulator(daqan_lords, latari_elves, fate_deck)

# Kör simuleringen av en runda
battle_simulator.simulate_round()