from factions import Faction, DaqanFaction, LatariFaction, NeutralFaction
from fate_deck import FateDeck
from battle import Battle
from players import HumanPlayer, RandomAIPlayer


random_ai_player_1 = RandomAIPlayer()
random_ai_player_2 = RandomAIPlayer()
human_player_1 = HumanPlayer()
human_player_2 = HumanPlayer()

daqan_lords = DaqanFaction(random_ai_player_1)
latari_elves = LatariFaction(random_ai_player_2)

daqan_lords.add_footman(3)
daqan_lords.add_bowman(2)
daqan_lords.add_knight(2)
daqan_lords.add_siege_tower(1)
daqan_lords.add_beastman(1)
daqan_lords.add_hellhound(1)
daqan_lords.add_dragon(4)

latari_elves.add_archer(4)
latari_elves.add_sorceress(1)
latari_elves.add_warrior(2)
latari_elves.add_pegasus_rider(1)
latari_elves.add_razorwing(1)
latari_elves.add_sorcerer(2)
latari_elves.add_giant(4)



fate_deck = FateDeck()

battle = Battle(daqan_lords, latari_elves, fate_deck)

battle.resolve_battle()