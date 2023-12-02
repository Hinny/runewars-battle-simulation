import random
from unit_types import Bowman, Footman, Knight, SiegeTower, Archer, PegasusRider, Sorceress, Warrior, Sorcerer, Razorwing, Beastman, Hellhound, Dragon, Giant

class Faction:
    def __init__(self, name, player, influence, tactic_cards, strength):
        self.name = name
        self.unit_types = []
        self.player = player
        self.influence = influence
        self.tactic_cards = tactic_cards
        self.strength = strength
        self.player.set_faction(self)

    def add_influence(self, influence):
         self.influence += influence

    def remove_influence(self, influence):
         self.influence -= influence

    def add_tactic_cards(self, tactic_cards):
         self.tactic_cards += tactic_cards

    def remove_tactic_cards(self, tactic_cards):
         self.tactic_cards -= tactic_cards

    def add_strength(self, strength):
         self.strength += strength

    def remove_strength(self, strength):
         self.strength -= strength

class DaqanFaction(Faction):
    def __init__(self, player):
        super().__init__("Daqan Lords", player, 3, 2, 0)

    def add_bowman(self, quantity):
         self.unit_types.append(Bowman(self, quantity))

    def add_footman(self, quantity):
         self.unit_types.append(Footman(self, quantity))

    def add_knight(self, quantity):
         self.unit_types.append(Knight(self, quantity))

    def add_siege_tower(self, quantity):
         self.unit_types.append(SiegeTower(self, quantity))

    def add_sorcerer(self, quantity):
         self.unit_types.append(Sorcerer(self, quantity))

    def add_razorwing(self, quantity):
         self.unit_types.append(Razorwing(self, quantity))

    def add_beastman(self, quantity):
         self.unit_types.append(Beastman(self, quantity))

    def add_hellhound(self, quantity):
         self.unit_types.append(Hellhound(self, quantity))

    def add_dragon(self, quantity):
         self.unit_types.append(Dragon(self, quantity))

    def add_giant(self, quantity):
         self.unit_types.append(Giant(self, quantity))

class LatariFaction(Faction):
    def __init__(self, player):
        super().__init__("Latari Elves", player, 4, 1, 0)

    def add_archer(self, quantity):
         self.unit_types.append(Archer(self, quantity))

    def add_pegasus_rider(self, quantity):
         self.unit_types.append(PegasusRider(self, quantity))

    def add_sorceress(self, quantity):
         self.unit_types.append(Sorceress(self, quantity))

    def add_warrior(self, quantity):
         self.unit_types.append(Warrior(self, quantity))

    def add_sorcerer(self, quantity):
         self.unit_types.append(Sorcerer(self, quantity))

    def add_razorwing(self, quantity):
         self.unit_types.append(Razorwing(self, quantity))

    def add_beastman(self, quantity):
         self.unit_types.append(Beastman(self, quantity))

    def add_hellhound(self, quantity):
         self.unit_types.append(Hellhound(self, quantity))

    def add_dragon(self, quantity):
         self.unit_types.append(Dragon(self, quantity))

    def add_giant(self, quantity):
         self.unit_types.append(Giant(self, quantity))

class NeutralFaction(Faction):
    def __init__(self, player):
        super().__init__("Neutral", player, 0, 0, 0)

    def add_sorcerer(self, quantity):
         self.unit_types.append(Sorcerer(self, quantity))

    def add_razorwing(self, quantity):
         self.unit_types.append(Razorwing(self, quantity))

    def add_beastman(self, quantity):
         self.unit_types.append(Beastman(self, quantity))

    def add_hellhound(self, quantity):
         self.unit_types.append(Hellhound(self, quantity))

    def add_dragon(self, quantity):
         self.unit_types.append(Dragon(self, quantity))

    def add_giant(self, quantity):
         self.unit_types.append(Giant(self, quantity))
