import random
from fate_deck import FateDeck
from faction import Faction
from unit_type import UnitType, Unit

class Battle:
    def __init__(self, attacker_faction, defender_faction, fate_deck):
        self.attacker_faction = attacker_faction
        self.defender_faction = defender_faction
        self.fate_deck = fate_deck

    def resolve_battle(self):
        print("₪" * 79)
        self.print_centered_line("Start of Battle", "₪")
        self.print_battle_status(self.attacker_faction, self.defender_faction)

        round_number = 1
        # Loop through all the initative values
        for initiative in range(1, 6):
            self.print_centered_line("INITIATIVE (🗲 ) " + str(initiative), "═")

            while True:
                # Sort out unit_types that has at least 1 standing unit that has not been already activated and that belongs to this initiative
                standing_not_activated_attacker_unit_types = [
                    unit_type for unit_type in self.attacker_faction.unit_types
                    if unit_type.initiative == initiative and (unit_type.get_number_of_available_units() > 0)
                ]

                standing_not_activated_defender_unit_types = [
                    unit_type for unit_type in self.defender_faction.unit_types
                    if unit_type.initiative == initiative and (unit_type.get_number_of_available_units() > 0)
                ]

                # Randomy select unit types from the available
                if len(standing_not_activated_attacker_unit_types) > 1:
                    attacker_unit_type_choice = self.attacker_faction.player.choose_next_activating_unit_type(standing_not_activated_attacker_unit_types)
                elif len(standing_not_activated_attacker_unit_types) == 1:
                    attacker_unit_type_choice = standing_not_activated_attacker_unit_types[0]
                else:
                    attacker_unit_type_choice = None

                if len(standing_not_activated_defender_unit_types) > 1:
                    defender_unit_type_choice = self.defender_faction.player.choose_next_activating_unit_type(standing_not_activated_defender_unit_types)
                elif len(standing_not_activated_defender_unit_types) == 1:
                    defender_unit_type_choice = standing_not_activated_defender_unit_types[0]
                else:
                    defender_unit_type_choice = None

                # If at least one of the attacker or defender unit types was selected, perform a sub step
                if attacker_unit_type_choice or defender_unit_type_choice:
                    self.print_centered_line("Battle Round " + str(round_number), "┈")
                    print()
                    self.resolve_battle_round(attacker_unit_type_choice, defender_unit_type_choice)
                    print()
                    self.print_centered_line("Status After Round " + str(round_number), " ")
                    self.print_battle_status(self.attacker_faction, self.defender_faction)
                    round_number += 1
                else:
                    break
  
        winner, attacker_strength, defender_strength = self.calculate_battle_resolution(self.attacker_faction, self.defender_faction)
        return winner, attacker_strength, defender_strength

    def resolve_battle_round(self, attacker_unit_type, defender_unit_type):
        attacker_damage = 0
        attacker_rout = 0
        attacker_orb = 0
        defender_damage = 0
        defender_rout = 0
        defender_orb = 0
        attacker_text = "None"
        defender_text = "None"

        if attacker_unit_type:
            attacker_text = str(attacker_unit_type.get_number_of_available_units()) + " x " + attacker_unit_type.name
            attacker_hand = self.fate_deck.draw_hand(len(attacker_unit_type.units))
            (attacker_damage, attacker_rout, attacker_orb) = self.fate_deck.calculate_total_results(attacker_hand, attacker_unit_type.shape)
        if defender_unit_type:
            defender_text = str(defender_unit_type.get_number_of_available_units()) + " x " + defender_unit_type.name
            defender_hand = self.fate_deck.draw_hand(len(defender_unit_type.units))
            (defender_damage, defender_rout, defender_orb) = self.fate_deck.calculate_total_results(defender_hand, defender_unit_type.shape)
    
        self.print_centered_line(attacker_text + " | " + defender_text, " ")       
        print()

        for _ in range(0, attacker_orb):
            print(" - " + self.attacker_faction.name + " " + attacker_unit_type.name + " performs " + attacker_unit_type.special_ability) #TODO: replace with actual ability

        for _ in range(0, defender_orb):
            print(" - " + self.defender_faction.name + " " + defender_unit_type.name + " performs " + defender_unit_type.special_ability) #TODO: replace with actual ability

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

    def calculate_battle_resolution(self, attacker_faction, defender_faction):
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

        print("━" * 79)
        print()
        print(attacker_faction.name + "'s final strenght is " + str(attacker_strength))
        print(defender_faction.name + "'s final strenght is " + str(defender_strength))
        print()
        print("˚₊‧⁺˖✮ The winner is " + winner + "! ✮˖⁺‧₊˚")
        print()
        print("₪" * 79)
        return winner, attacker_strength, defender_strength

    def print_battle_status(self, attacker_faction, defender_faction):
        """
        Prints the current status of the battle in the terminal.
        Each unit is represented with its type, initiative, health, shape, and damage/routed status.
        The damage and routed status are aligned independently of the length of the unit type name.
        """
        print()
        print(f"Attacker: {attacker_faction.name:<29} | Defender: {defender_faction.name:<30}")
        
        # Gather units for both factions
        attacker_units = [unit for unit_type in attacker_faction.unit_types for unit in unit_type.units]
        defender_units = [unit for unit_type in defender_faction.unit_types for unit in unit_type.units]

        # Determine the maximum length for alignment
        max_units_length = max(len(attacker_units), len(defender_units))

        # Print units side by side
        for i in range(max_units_length):
            attacker_unit_str = attacker_units[i].get_line_str() if i < len(attacker_units) else ''
            defender_unit_str = defender_units[i].get_line_str() if i < len(defender_units) else ''
            print(f"{attacker_unit_str:<39} | {defender_unit_str}")
        
        print()

    def print_centered_line(self, text, padding_char):
        """
        Prints a line of 79 characters with the text string centered and padded with the padding character.
        There will be a whitespace on each side of the text string.
        """
        # Total length of the line
        total_length = 79

        # Ensuring that the text is surrounded by a whitespace on each side
        text = f" {text} "

        # Calculate the amount of padding needed on each side
        padding_length = (total_length - len(text)) // 2

        # Constructing the line
        line = padding_char * padding_length + text + padding_char * padding_length

        # Adjust if the total length is not 79 due to odd division
        if len(line) < total_length:
            line += padding_char

        # Printing the line
        print(line)
