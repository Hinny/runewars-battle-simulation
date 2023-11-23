import random
from factions import Faction

class PlayerInterface:
    def __init__(self):
        self.faction = None

    def set_faction(self, faction):
        self.faction = faction

    def choose_unit_type(self, unit_types):
        raise NotImplementedError

    def choose_unit(self, eligible_units):
        raise NotImplementedError

class HumanPlayer(PlayerInterface):
    def choose_unit_type(self, unit_types):
        print(f"          {self.faction.name}, choose a unit type:")
        return self.choose_unit_type_from_list(unit_types)

    def choose_unit(self, units):
        print(f"          {self.faction.name}, choose a unit:")
        return self.choose_unit_from_list(units)

    def choose_unit_type_from_list(self, unit_types):
        for i, unit_type in enumerate(unit_types):
            print(f"           {i+1}. {unit_type.faction.name} {unit_type}")
        choice = self.get_user_choice(len(unit_types))
        return unit_types[choice - 1]

    def choose_unit_from_list(self, units):
        for i, unit in enumerate(units):
            print(f"           {i+1}. {unit.unit_type.faction.name} {unit}")
        choice = self.get_user_choice(len(units))
        return units[choice - 1]

    def get_user_choice(self, max_number):
        valid_choice = False
        while not valid_choice:
            try:
                choice = int(input("Your choice: "))
                if 1 <= choice <= max_number:
                    valid_choice = True
                else:
                    print("Invalid choice, try again.")
            except ValueError:
                print("Invalid input, try again.")
        return choice

class RandomAIPlayer(PlayerInterface):
    def choose_unit_type(self, unit_types):
        return random.choice(unit_types)

    def choose_unit(self, units):
        return random.choice(units)