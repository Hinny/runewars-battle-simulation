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
            unit = Unit()
            self.units.append(unit)
    
class Unit:
    def __init__(self):
        self.damageTokens = 0
        self.isStanding = True
        self.hasActivated = False

    def take_one_damage(self):
        self.damageTokens += 1
        
    def rout(self):
        self.isStanding = False
    
    def activate(self):
        self.hasActivated = True
    
class Bowman(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Bowman", "triangle", 1, "Concentrated Fire", 1, 8, number_of_units)

class Footman(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Footman", "triangle", 1, "Valiant Strike", 3, 16, number_of_units)

class Knight(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Knight", "rectangle", 2, "Command", 2, 8, number_of_units)

class Archer(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Archer", "triangle", 1, "Crack Shot", 1, 16, number_of_units)

class PegasusRider(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Pegasus Rider", "rectangle", 3, "Charge", 2, 4, number_of_units)

class Sorcerer(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Sorcerer", "circle", 1, "Undying", 1, 8, number_of_units)

class Beastman(UnitType):
    def __init__(self, number_of_units):
        super().__init__("Beastman", "triangle", 1, "Roar", 2, 8, number_of_units)
