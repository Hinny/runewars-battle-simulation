
from log_config import setup_loggers
detailed_logger, summary_logger = setup_loggers()

class Battle:
    def __init__(self, attacker_faction, defender_faction, fate_deck):
        self.attacker_faction = attacker_faction
        self.defender_faction = defender_faction
        self.fate_deck = fate_deck

    def resolve_battle(self):
        detailed_logger.info("=" * 79)
        start_of_battle_line = self.format_centered_line("Start of Battle", "=")
        detailed_logger.info(start_of_battle_line)
        self.print_legend()
        self.print_battle_status(self.attacker_faction, self.defender_faction)
        self.log_summary_start(self.attacker_faction, self.defender_faction)
        round_number = 1
        # Loop through all the initative values
        for initiative in range(1, 6):
            initiative_line = self.format_centered_line("INITIATIVE (I) " + str(initiative), "=")
            detailed_logger.info(initiative_line)
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
                    attacker_unit_type_choice = self.attacker_faction.player.choose_unit_type(standing_not_activated_attacker_unit_types)
                elif len(standing_not_activated_attacker_unit_types) == 1:
                    attacker_unit_type_choice = standing_not_activated_attacker_unit_types[0]
                else:
                    attacker_unit_type_choice = None

                if len(standing_not_activated_defender_unit_types) > 1:
                    defender_unit_type_choice = self.defender_faction.player.choose_unit_type(standing_not_activated_defender_unit_types)
                elif len(standing_not_activated_defender_unit_types) == 1:
                    defender_unit_type_choice = standing_not_activated_defender_unit_types[0]
                else:
                    defender_unit_type_choice = None

                # If at least one of the attacker or defender unit types was selected, perform a sub step
                if attacker_unit_type_choice or defender_unit_type_choice:
                    battle_round_line = self.format_centered_line("Battle Round " + str(round_number), "~")
                    detailed_logger.debug(battle_round_line)

                    detailed_logger.debug("")
                    self.resolve_battle_round(attacker_unit_type_choice, defender_unit_type_choice)
                    detailed_logger.debug("")
                    status_header_line = self.format_centered_line("Status After Round " + str(round_number), " ")
                    detailed_logger.info(status_header_line)
                    self.print_battle_status(self.attacker_faction, self.defender_faction)
                    round_number += 1
                else:
                    break

        winner, attacker_strength, defender_strength = self.calculate_battle_resolution(self.attacker_faction, self.defender_faction)
        self.log_summary_end(winner, attacker_strength, defender_strength, self.attacker_faction, self.defender_faction)
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
        attacker_hand = []
        defender_hand = []

        if attacker_unit_type:
            attacker_text = str(attacker_unit_type.get_number_of_available_units()) + " x " + attacker_unit_type.name
            attacker_hand = self.fate_deck.draw_hand(len(attacker_unit_type.units))
            (attacker_damage, attacker_rout, attacker_orb) = self.fate_deck.calculate_total_results(attacker_hand, attacker_unit_type.shape)
        if defender_unit_type:
            defender_text = str(defender_unit_type.get_number_of_available_units()) + " x " + defender_unit_type.name
            defender_hand = self.fate_deck.draw_hand(len(defender_unit_type.units))
            (defender_damage, defender_rout, defender_orb) = self.fate_deck.calculate_total_results(defender_hand, defender_unit_type.shape)

        result_header_line = self.format_centered_line(attacker_text + " | " + defender_text, " ")
        detailed_logger.debug(result_header_line)

        detailed_logger.debug("")
        detailed_logger.debug(f"{self.attacker_faction.name} draws {len(attacker_hand)} Fate cards")
        detailed_logger.debug(f"{self.defender_faction.name} draws {len(defender_hand)} Fate cards")
        detailed_logger.debug("")

        detailed_logger.debug(f"{self.attacker_faction.name} reveals {attacker_orb} orb results")
        detailed_logger.debug(f"{self.defender_faction.name} reveals {defender_orb} orb results")
        detailed_logger.debug("")
        for i in range(0, attacker_orb):
            detailed_logger.debug(f" - {self.attacker_faction.name} {attacker_unit_type.name} performs {attacker_unit_type.special_ability.name}")
            if i == 0:
                detailed_logger.debug(f"   ({attacker_unit_type.special_ability.description})")
            attacker_unit_type.special_ability.resolve(self.attacker_faction, self.defender_faction)
        if attacker_orb:
            detailed_logger.debug("")
        for i in range(0, defender_orb):
            detailed_logger.debug(f" - {self.defender_faction.name} {defender_unit_type.name} performs {defender_unit_type.special_ability.name}")
            if i == 0:
                detailed_logger.debug(f"   ({defender_unit_type.special_ability.description})")
            defender_unit_type.special_ability.resolve(self.defender_faction, self.attacker_faction)
        if defender_orb:
            detailed_logger.debug("")

        detailed_logger.debug(f"{self.attacker_faction.name} reveals {attacker_rout} rout results")
        detailed_logger.debug(f"{self.defender_faction.name} reveals {defender_rout} rout results")
        detailed_logger.debug("")
        for _ in range(0, attacker_rout):
            detailed_logger.debug(f" - {self.attacker_faction.name} {attacker_unit_type.name} deals 1 rout (#)")
            attacker_unit_type.regular_rout.resolve(self.attacker_faction, self.defender_faction)
        if attacker_rout:
            detailed_logger.debug("")
        for _ in range(0, defender_rout):
            detailed_logger.debug(f" - {self.defender_faction.name} {defender_unit_type.name} deals 1 rout (#)")
            defender_unit_type.regular_rout.resolve(self.defender_faction, self.attacker_faction)
        if defender_rout:
            detailed_logger.debug("")

        detailed_logger.debug(f"{self.attacker_faction.name} reveals {attacker_damage} damage results")
        detailed_logger.debug(f"{self.defender_faction.name} reveals {defender_damage} damage results")
        detailed_logger.debug("")
        for _ in range(0, attacker_damage):
            detailed_logger.debug(f" - {self.attacker_faction.name} {attacker_unit_type.name} deals 1 damage (o)")
            attacker_unit_type.regular_damage.resolve(self.attacker_faction, self.defender_faction)
        if attacker_damage:
            detailed_logger.debug("")
        for _ in range(0, defender_damage):
            detailed_logger.debug(f" - {self.defender_faction.name} {defender_unit_type.name} deals 1 damage (o)")
            defender_unit_type.regular_damage.resolve(self.defender_faction, self.attacker_faction)
        if defender_damage:
            detailed_logger.debug("")
        if attacker_unit_type:
            for unit in attacker_unit_type.units:
                unit.has_activated = True
            self.fate_deck.discard_hand(attacker_hand)

        if defender_unit_type:
            for unit in defender_unit_type.units:
                unit.has_activated = True
            self.fate_deck.discard_hand(defender_hand)

    def calculate_battle_resolution(self, attacker_faction, defender_faction):
        # Function to calculate the strength of a faction
        def calculate_unit_strength(faction):
            unit_strength = 0
            for unit_type in faction.unit_types:
                if unit_type.shape == 'hexagon':
                    # All hexagon units count towards strength
                    unit_strength += len(unit_type.units)
                else:
                    # Only standing units count towards strength
                    unit_strength += sum(1 for unit in unit_type.units if unit.is_standing)
            return unit_strength

                # Count strength for both attacker and defender
        attacker_unit_strength = calculate_unit_strength(attacker_faction)
        defender_unit_strength = calculate_unit_strength(defender_faction)

        attacker_strength = attacker_unit_strength + attacker_faction.strength
        defender_strength = defender_unit_strength + defender_faction.strength

        # Determine the winner
        if attacker_strength > defender_strength:
            winner = attacker_faction
        elif defender_strength > attacker_strength:
            winner = defender_faction
        else:
            # In case of a tie, the defender wins
            winner = defender_faction

        detailed_logger.debug("~" * 79)
        detailed_logger.debug("")
        detailed_logger.debug(attacker_faction.name + " unit strenght is " + str(attacker_unit_strength))
        detailed_logger.debug(defender_faction.name + " unit strenght is " + str(defender_unit_strength))
        detailed_logger.debug("")

        if attacker_faction.strength > 0:
            detailed_logger.debug(attacker_faction.name + " forification bonus is " + str(attacker_faction.strength))
        if defender_faction.strength > 0:
            detailed_logger.debug(defender_faction.name + " forification bonus is " + str(defender_faction.strength))
        if attacker_faction.strength > 0 or defender_faction.strength > 0:
            detailed_logger.debug("")

        detailed_logger.info(attacker_faction.name + " final strenght is " + str(attacker_strength))
        detailed_logger.info(defender_faction.name + " final strenght is " + str(defender_strength))
        detailed_logger.debug("")
        detailed_logger.info(f" ---=== The winner is {winner.name} ({winner.player.name})! ===---")
        detailed_logger.debug("")
        detailed_logger.debug("=" * 79)

        return winner, attacker_strength, defender_strength

    def print_legend(self):
        legend_header_line = self.format_centered_line("Legend", "~")
        detailed_logger.debug(legend_header_line)
        detailed_logger.debug("I = Initiative")
        detailed_logger.debug("@ = Health")
        detailed_logger.debug("T = Triangle")
        detailed_logger.debug("C = Circle")
        detailed_logger.debug("R = Rectangle")
        detailed_logger.debug("H = Hexagon")
        detailed_logger.debug("o = Damage")
        detailed_logger.debug("# = Routed")
        detailed_logger.debug("X = Activated")
        detailed_logger.debug("~" * 79)

    def print_battle_status(self, attacker_faction, defender_faction):
        detailed_logger.info("")
        detailed_logger.info(f"Attacker                                | Defender")
        detailed_logger.info(f"Faction: {attacker_faction.name:<30} | Faction: {defender_faction.name}")
        detailed_logger.info(f"Player: {attacker_faction.player.name:<31} | Player: {defender_faction.player. name}")

        # Gather units for both factions
        attacker_units = [unit for unit_type in attacker_faction.unit_types for unit in unit_type.units]
        defender_units = [unit for unit_type in defender_faction.unit_types for unit in unit_type.units]

        # Determine the maximum length for alignment
        max_units_length = max(len(attacker_units), len(defender_units))

        # Print units side by side
        for i in range(max_units_length):
            attacker_unit_str = attacker_units[i].get_line_str() if i < len(attacker_units) else ''
            defender_unit_str = defender_units[i].get_line_str() if i < len(defender_units) else ''
            detailed_logger.info(f"{attacker_unit_str:<39} | {defender_unit_str}")

        detailed_logger.info("")

    def format_centered_line(self, text, padding_char):
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
        return line

    def log_summary_start(self, attacker_faction, defender_faction):
        summary_logger.info(f"Attacker: {attacker_faction.name}")
        for unit_type in attacker_faction.unit_types:
            summary_logger.info(f"   {unit_type.name} x {len(unit_type.units)}")
        summary_logger.info(f"Defender: {defender_faction.name}")
        for unit_type in defender_faction.unit_types:
            summary_logger.info(f"   {unit_type.name} x {len(unit_type.units)}")
        summary_logger.info("")

    def log_summary_end(self, winner, attacker_strength, defender_strength, attacker_faction, defender_faction):
        summary_logger.info(f"{attacker_faction.name:<15}: {attacker_strength}")
        summary_logger.info(f"{defender_faction.name:<15}: {defender_strength}")
        summary_logger.info(f"Winner: {winner.name} ({winner.player.name})")
        summary_logger.info("~" * 30)
