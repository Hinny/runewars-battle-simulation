from special_abilities import RegularDamage, RegularRout, ConcentratedFire

class UnitType:
    def __init__(self, name, shape, health, special_ability, initiative, maxNumber, faction, number_of_units):
        self.name = name
        self.shape = shape
        self.health = health
        self.regular_damage = RegularDamage()
        self.regular_rout = RegularRout()
        self.special_ability = special_ability
        self.initiative = initiative
        self.maxNumber = maxNumber
        self.faction = faction
        self.units = []
        self.add_units(number_of_units)

    def __str__(self):
        return f"{self.name} {self.get_specs_str()}"

    def get_specs_str(self):
        return f"({self.initiative}🗲  {self.health}♥  {self.shape_symbol()} )"
    
    def shape_symbol(self):
        # Returnera motsvarande symbol för enhetens form
        shape_symbols = {
            'triangle': '▲',
            'circle': '●',
            'rectangle': '∎',
            'hexagon': '⬣'
        }
        return shape_symbols.get(self.shape, '?')  # Returnera '?' om formen inte finns
    
    def add_units(self, number_of_new_units):
        if number_of_new_units > self.maxNumber:
            number_of_new_units = self.maxNumber
        for _ in range(0, number_of_new_units):
            unit = Unit(self)
            self.units.append(unit)
            
    def get_number_of_available_units(self):
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
    
    def __str__(self):
        return f"{self.unit_type} {self.get_status_str()}"
    
    def get_line_str(self):
        # Bestäm kolumnbredder
        name_width = 16  # 15 tecken + 1 för blanksteg
        specs_width = 12  # Antaget bredd för specs (ex. " (5🗲 3♥ ⬣)")
        status_width = 7  # Antaget bredd för status (ex. "✖ ◉◉⚑")

        return f"{self.unit_type.name:<{name_width}}{self.unit_type.get_specs_str():<{specs_width}}{self.get_status_str():<{status_width}}"
    
    def get_status_str(self):
        activated_str = "✖" if self.has_activated else " "
        routed_str = "⚑" if not self.is_standing else " "
        damage_str = "◉" * self.damage_taken
        return f"{activated_str} {routed_str} {damage_str}"
    
# Daqan Unit Types   
class Bowman(UnitType):
    def __init__(self, faction, number_of_units):
        super().__init__("Bowman", "triangle", 1, ConcentratedFire(), 1, 8, faction, number_of_units)

class Footman(UnitType):
    def __init__(self, faction, number_of_units):
        super().__init__("Footman", "triangle", 1, RegularDamage(), 3, 16, faction, number_of_units)

class Knight(UnitType):
    def __init__(self, faction, number_of_units):
        super().__init__("Knight", "rectangle", 2, RegularDamage(), 2, 8, faction, number_of_units)

class SiegeTower(UnitType):
    def __init__(self, faction, number_of_units):
        super().__init__("Siege Tower", "hexagon", 3, RegularDamage(), 5, 4, faction, number_of_units)

# Latari Unit Types   
class Archer(UnitType):
    def __init__(self, faction, number_of_units):
        super().__init__("Archer", "triangle", 1, RegularDamage(), 1, 16, faction, number_of_units)

class PegasusRider(UnitType):
    def __init__(self, faction, number_of_units):
        super().__init__("Pegasus Rider", "rectangle", 3, RegularDamage(), 2, 4, faction, number_of_units)

class Sorceress(UnitType):
    def __init__(self, faction, number_of_units):
        super().__init__("Sorceress", "circle", 1, RegularDamage(), 3, 8, faction, number_of_units)

class Warrior(UnitType):
    def __init__(self, faction, number_of_units):
        super().__init__("Warrior", "rectangle", 2, RegularDamage(), 4, 8, faction, number_of_units)

# Waiqar Unit Types

# Uthuk Unit Types

# Neutral Unit Types
class Sorcerer(UnitType):
    def __init__(self, faction, number_of_units):
        super().__init__("Sorcerer", "circle", 1, RegularDamage(), 1, 8, faction, number_of_units)

class Razorwing(UnitType):
    def __init__(self, faction, number_of_units):
        super().__init__("Razorwing", "triangle", 1, RegularDamage(), 1, 8, faction, number_of_units)

class Beastman(UnitType):
    def __init__(self, faction, number_of_units):
        super().__init__("Beastman", "triangle", 1, RegularDamage(), 2, 8, faction, number_of_units)

class Hellhound(UnitType):
    def __init__(self, faction, number_of_units):
        super().__init__("Hellhound", "rectangle", 2, RegularDamage(), 3, 4, faction, number_of_units)

class Dragon(UnitType):
    def __init__(self, faction, number_of_units):
        super().__init__("Dragon", "hexagon", 4, RegularDamage(), 4, 4, faction, number_of_units)

class Giant(UnitType):
    def __init__(self, faction, number_of_units):
        super().__init__("Giant", "hexagon", 5, RegularDamage(), 5, 4, faction, number_of_units)
