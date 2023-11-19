class UnitType:
    def __init__(self, name, shape, health, special_ability, initiative, maxNumber, number_of_units):
        self.name = name
        self.shape = shape
        self.health = health
        self.special_ability = special_ability
        self.initiative = initiative
        self.maxNumber = maxNumber
        self.units = []
        self.add_units(number_of_units)
    
    def add_units(self, number_of_new_units):
        if number_of_new_units > self.maxNumber:
            number_of_new_units = self.maxNumber
        for _ in range(0, number_of_new_units):
            unit = Unit(self)
            self.units.append(unit)
            
    def number_of_available_units(self):
        """
        Returns the number of units of this unit type that are standing and have not activated.
        """
        return sum(1 for unit in self.units if unit.is_standing and not unit.has_activated)
    
class Unit:
    def __init__(self, unit_type):
        self.unit_type = unit_type
        self.damage_taken = 0
        self.is_standing = True
        self.has_activated = False

# Daqan Unit Types   
class Bowman(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Bowman", "triangle", 1, "Concentrated Fire", 1, 8, number_of_units)

class Footman(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Footman", "triangle", 1, "Valiant Strike", 3, 16, number_of_units)

class Knight(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Knight", "rectangle", 2, "Command", 2, 8, number_of_units)

class SiegeTower(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Siege Tower", "hexagon", 3, "Lay Siege", 5, 4, number_of_units)

# Latari Unit Types   
class Archer(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Archer", "triangle", 1, "Crack Shot", 1, 16, number_of_units)

class PegasusRider(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Pegasus Rider", "rectangle", 3, "Charge", 2, 4, number_of_units)

class Sorceress(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Sorceress", "circle", 1, "Word of Vaal", 3, 8, number_of_units)

class Warrior(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Warrior", "rectangle", 2, "Overpower", 4, 8, number_of_units)

# Waiqar Unit Types

# Uthuk Unit Types

# Neutral Unit Types
class Sorcerer(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Sorcerer", "circle", 1, "Undying", 1, 8, number_of_units)

class Razorwing(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Razorwing", "triangle", 1, "Stun", 1, 8, number_of_units)

class Beastman(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Beastman", "triangle", 1, "Roar", 2, 8, number_of_units)

class Hellhound(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Hellhound", "rectangle", 2, "Burning", 3, 4, number_of_units)

class Dragon(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Dragon", "hexagon", 4, "Flamming Breath", 4, 4, number_of_units)

class Giant(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Giant", "hexagon", 5, "Rage", 5, 4, number_of_units)
