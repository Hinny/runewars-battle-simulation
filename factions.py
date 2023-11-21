import random

class Faction:
    def __init__(self, name, player):
        self.name = name
        self.unit_types = []
        self.player = player

    def add_unit_type(self, unit_type):
        self.unit_types.append(unit_type)

