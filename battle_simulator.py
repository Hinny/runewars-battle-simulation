import random
from fate_deck import FateDeck
from factions import Faction
from units import UnitType, Unit

class BattleSimulator:
    def __init__(self, attacker_faction, defender_faction, fate_deck):
        self.attacker_faction = attacker_faction
        self.defender_faction = defender_faction
        self.fate_deck = fate_deck

    def battle(self):

        print("--== Start of Battle ==--")
        self.print_battle_status(self.attacker_faction, self.defender_faction)

        # Organizer the attacker's units according to initiativ
        attacker_unit_types_by_initiative = {}
        for unit_type in self.attacker_faction.unit_types:
            initiative = unit_type.initiative
            if initiative not in attacker_unit_types_by_initiative:
                attacker_unit_types_by_initiative[initiative] = []
            attacker_unit_types_by_initiative[initiative].append(unit_type)

        # Organizer the defender's units according to initiativ
        defender_unit_types_by_initiative = {}
        for unit_type in self.defender_faction.unit_types:
            initiative = unit_type.initiative
            if initiative not in defender_unit_types_by_initiative:
                defender_unit_types_by_initiative[initiative] = []
            defender_unit_types_by_initiative[initiative].append(unit_type)

        round_number = 1
        # Loop through all the initative values
        for initiative in range(1, 6):

            more_units_to_activate = True

            while more_units_to_activate:
                # Sort out unit_types that has at least 1 standing unit that has not been already activated and that belongs to this initiative
                standing_not_activated_attacker_unit_types = [
                    unit_type for unit_type in self.attacker_faction.unit_types
                    if unit_type.initiative == initiative and 
                    any(unit.is_standing and not unit.has_activated for unit in unit_type.units)
                ]

                standing_not_activated_defender_unit_types = [
                    unit_type for unit_type in self.defender_faction.unit_types
                    if unit_type.initiative == initiative and 
                    any(unit.is_standing and not unit.has_activated for unit in unit_type.units)
                ]

                # Randomy select unit types from the available
                if standing_not_activated_attacker_unit_types:
                    attacker_unit_type_choice = random.choice(standing_not_activated_attacker_unit_types)
                else:
                    attacker_unit_type_choice = None

                if standing_not_activated_defender_unit_types:
                    defender_unit_type_choice = random.choice(standing_not_activated_defender_unit_types)
                else:
                    defender_unit_type_choice = None

                # If at least one of the attacker or defender unit types was selected, perform a sub step
                if attacker_unit_type_choice or defender_unit_type_choice:
                    print("--== Round " + str(round_number) + " ==--")
                    self.perform_battle_round(attacker_unit_type_choice, defender_unit_type_choice)
                    print("--== Status After Round " + str(round_number) + " ==--")
                    self.print_battle_status(self.attacker_faction, self.defender_faction)
                    round_number += 1
                else:
                    more_units_to_activate = False
        
        print("--== End of Battle ==--")
        self.print_battle_status(self.attacker_faction, self.defender_faction)

        winner = self.resolve_battle(self.attacker_faction, self.defender_faction)
        print("The winner is " + winner + "!")

    def perform_battle_round(self, attacker_unit_type, defender_unit_type):
        attacker_damage = 0
        attacker_rout = 0
        attacker_orb = 0
        defender_damage = 0
        defender_rout = 0
        defender_orb = 0
        attacker_text = "None"
        defender_text = "None"

        if attacker_unit_type:
            attacker_text = str(attacker_unit_type.number_of_available_units()) + "x" + attacker_unit_type.name
            attacker_hand = self.fate_deck.draw_hand(len(attacker_unit_type.units))
            (attacker_damage, attacker_rout, attacker_orb) = self.fate_deck.calculate_total_results(attacker_hand, attacker_unit_type.shape)
        if defender_unit_type:
            defender_text = str(defender_unit_type.number_of_available_units()) + "x" + defender_unit_type.name
            defender_hand = self.fate_deck.draw_hand(len(defender_unit_type.units))
            (defender_damage, defender_rout, defender_orb) = self.fate_deck.calculate_total_results(defender_hand, defender_unit_type.shape)

        for _ in range(0, attacker_orb):
            print("Performing " + attacker_unit_type.special_ability) #TODO: replace with actual ability

        for _ in range(0, defender_orb):
            print("Performing " + defender_unit_type.special_ability) #TODO: replace with actual ability

        if (attacker_rout > 0):
            self.defender_faction.deal_rout(attacker_rout)
        if (defender_rout > 0):
            self.attacker_faction.deal_rout(defender_rout)

        if (attacker_damage > 0):
            self.defender_faction.deal_damage(attacker_damage)
        if (defender_damage > 0):
            self.attacker_faction.deal_damage(defender_damage)

        if attacker_unit_type:
            for unit in attacker_unit_type.units:
                unit.has_activated = True
            self.fate_deck.discard_hand(attacker_hand)
        
        if defender_unit_type:
            for unit in defender_unit_type.units:
                unit.has_activated = True
            self.fate_deck.discard_hand(defender_hand)

    def print_battle_status(self, attacker_faction, defender_faction):
        """
        Prints the current status of the battle in the terminal.
        Each unit is represented with its type, initiative, health, shape, and damage/routed status.
        The damage and routed status are aligned independently of the length of the unit type name.
        """
        print(f"Attacker: {attacker_faction.name:<30} | Defender: {defender_faction.name:<30}")
        
        # Function to create a string representation of a unit
        def unit_to_string(unit):
            health_symbol = '♥'
            shape_symbol = {'triangle': '▲', 'circle': '⬤', 'rectangle': '▮', 'hexagon': '⬣'}[unit.unit_type.shape]
            unit_info = f"{unit.unit_type.name} (I{unit.unit_type.initiative}- {unit.unit_type.health}{health_symbol}-{shape_symbol} )"
            damage_symbols = '◉' * unit.damage_taken + '⚑' * (not unit.is_standing)
            return f"{unit_info:<25} {damage_symbols:>10}"

        # Gather units for both factions
        attacker_units = [unit for unit_type in attacker_faction.unit_types for unit in unit_type.units]
        defender_units = [unit for unit_type in defender_faction.unit_types for unit in unit_type.units]

        # Determine the maximum length for alignment
        max_units_length = max(len(attacker_units), len(defender_units))

        # Print units side by side
        for i in range(max_units_length):
            attacker_unit_str = unit_to_string(attacker_units[i]) if i < len(attacker_units) else ''
            defender_unit_str = unit_to_string(defender_units[i]) if i < len(defender_units) else ''
            print(f"{attacker_unit_str:<40} | {defender_unit_str}")

        print("-" * 79)

    def resolve_battle(self, attacker_faction, defender_faction):
        """
        Resolves the battle by counting the number of standing units for both factions.
        Units with shape 'hexagon' contribute to strength even if routed.
        The faction with the most strength is declared the winner.
        In case of a tie, the defender is declared the winner.
        """
        # Function to calculate the strength of a faction
        def calculate_strength(faction):
            strength = 0
            for unit_type in faction.unit_types:
                if unit_type.shape == 'hexagon':
                    # All hexagon units count towards strength
                    strength += len(unit_type.units)
                else:
                    # Only standing units count towards strength
                    strength += sum(1 for unit in unit_type.units if unit.is_standing)
            return strength

        # Count strength for both attacker and defender
        attacker_strength = calculate_strength(attacker_faction)
        defender_strength = calculate_strength(defender_faction)

        # Determine the winner
        if attacker_strength > defender_strength:
            winner = attacker_faction.name
        elif defender_strength > attacker_strength:
            winner = defender_faction.name
        else:
            # In case of a tie, the defender wins
            winner = defender_faction.name

        return winner
