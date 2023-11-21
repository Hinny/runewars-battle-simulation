import random

class PlayerInterface:
    def choose_next_activating_unit_type(self, unit_types):
        raise NotImplementedError
    
    def choose_own_unit_for_regular_damage(self, eligible_units):
        raise NotImplementedError
    
    def choose_own_unit_for_regular_rout(self, eligible_units):
        raise NotImplementedError

class HumanPlayer(PlayerInterface):
    def choose_next_activating_unit_type(self, unit_types):
        print("          Choose a unit type to activate:")
        return self.choose_unit_type_from_list(unit_types)

    def choose_own_unit_for_regular_damage(self, eligible_units):
        print("          Choose a unit to take 1 damage:")
        return self.choose_unit_from_list(eligible_units)

    def choose_own_unit_for_regular_rout(self, eligible_units):
        print("          Choose a unit to be routed:")
        return self.choose_unit_from_list(eligible_units)

    def choose_unit_type_from_list(self, unit_types):
        for i, unit_type in enumerate(unit_types):
            print(f"          {i+1}. {unit_type.faction.name} {unit_type} x {unit_type.get_number_of_available_units()}")
        choice = self.get_user_choice(len(unit_types))
        return unit_types[choice - 1]
    
    def choose_unit_from_list(self, units):
        for i, unit in enumerate(units):
            print(f"          {i+1}. {unit.unit_type.faction.name} {unit}")                  
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
    def choose_next_activating_unit_type(self, unit_types):
        return random.choice(unit_types)
    
    def choose_own_unit_for_regular_damage(self, eligible_units):
        return random.choice(eligible_units)
    
    def choose_own_unit_for_regular_rout(self, eligible_units):
        return random.choice(eligible_units)
