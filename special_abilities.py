import random

class SpecialAbility:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def resolve(self, your_faction, opponent_faction):
        raise NotImplementedError

    def get_units_regular_damage_priority(self, faction):
        all_units = [u for faction.unit_type in faction.unit_types for u in faction.unit_type.units]

        damaged_units = [u for u in all_units if u.damage_taken > 0]
        standing_units = [u for u in all_units if u.is_standing and u.damage_taken == 0]
        routed_units = [u for u in all_units if not u.is_standing]

        if damaged_units:
            eligible_units = damaged_units
        elif standing_units:
            eligible_units = standing_units
        elif routed_units:
            eligible_units = routed_units
        else:
            eligible_units = []

        return eligible_units

    def get_units_regular_rout_priority(self, faction):
        # Gather all standing units
        standing_units = [u for faction.unit_type in faction.unit_types for u in faction.unit_type.units if u.is_standing]

        # Sort units according to priority: first undamaged standing units, then damaged standing units
        undamaged_standing_units = [u for u in standing_units if u.damage_taken == 0]
        damaged_standing_units = [u for u in standing_units if u.damage_taken > 0]

        if undamaged_standing_units:
            eligible_units = undamaged_standing_units
        elif damaged_standing_units:
            eligible_units = damaged_standing_units
        else:
            eligible_units = []

        return eligible_units

    def get_all_units(self, faction):
        eligible_units = [u for faction.unit_type in faction.unit_types for u in faction.unit_type.units]

        return eligible_units

    def get_standing_triangle_units(self, faction):
        eligible_units = [u for faction.unit_type in faction.unit_types for u in faction.unit_type.units if u.is_standing and u.unit_type.shape == "triangle"]

        return eligible_units

class RegularDamage(SpecialAbility):
    def __init__(self):
        self.name = "Damage"
        self.description = "Deal 1 damage (◉ )."

    def resolve(self, your_faction, opponent_faction):
        eligible_units = self.get_units_regular_damage_priority(opponent_faction)

        if len(eligible_units) > 1:
            target_unit = opponent_faction.player.choose_unit(eligible_units)
        elif len(eligible_units) == 1:
            target_unit = eligible_units[0]
        else:
            print(f"   No eligible target units.")
            return

        target_unit.damage_unit()

class RegularRout(SpecialAbility):
    def __init__(self):
        self.name = "Rout"
        self.description = "Deal 1 rout (⚑ )."

    def resolve(self, your_faction, opponent_faction):
        eligible_units = self.get_units_regular_rout_priority(opponent_faction)

        if len(eligible_units) > 1:
            target_unit = opponent_faction.player.choose_unit(eligible_units)
        elif len(eligible_units) == 1:
            target_unit = eligible_units[0]
        else:
            print(f"   No eligible target units.")
            return

        target_unit.rout_unit()

class ConcentratedFire(SpecialAbility):
    def __init__(self):
        self.name = "Concentrated Fire"
        self.description = "Deal 1 damage (◉ ). Your opponent must assign this to a unit with more than 1 health (♥), if able."

    def resolve(self, your_faction, opponent_faction):
        eligible_units = self.get_unit_more_health_damage_priority(opponent_faction)

        if len(eligible_units) > 1:
            target_unit = opponent_faction.player.choose_unit(eligible_units)
        elif len(eligible_units) == 1:
            target_unit = eligible_units[0]
        else:
            print(f"   No eligible target units.")
            return

        target_unit.damage_unit()

    def get_unit_more_health_damage_priority(self, faction):
        # Gather all units
        all_units = [u for faction.unit_type in faction.unit_types for u in faction.unit_type.units]
        # Sort units according to priority: first damaged, then standing, then routed
        damaged_units = [u for u in all_units if u.damage_taken > 0]
        standing_units_with_high_health = [u for u in all_units if u.is_standing and u.damage_taken == 0 and u.unit_type.health > 1]
        standing_units_with_low_health = [u for u in all_units if u.is_standing and u.damage_taken == 0 and u.unit_type.health == 1]
        routed_units_with_high_health = [u for u in all_units if not u.is_standing and u.unit_type.health > 1]
        routed_units_with_low_health = [u for u in all_units if not u.is_standing and u.unit_type.health == 1]

        if damaged_units:
            eligible_units = damaged_units
        elif standing_units_with_high_health:
            eligible_units = standing_units_with_high_health
        elif standing_units_with_low_health:
            eligible_units = standing_units_with_low_health
        elif routed_units_with_high_health:
            eligible_units = routed_units_with_high_health
        elif routed_units_with_low_health:
            eligible_units = routed_units_with_low_health
        else:
            eligible_units = []

        return eligible_units

class ValiantStrike(SpecialAbility):
    def __init__(self):
        self.name = "Valiant Strike"
        self.description = "Deal 1 damage (◉ ). If this does not defeate the unit, it is dealt an additional 1 damage (◉ )."

    def resolve(self, your_faction, opponent_faction):
        eligible_units = self.get_units_regular_damage_priority(opponent_faction)

        if len(eligible_units) > 1:
            target_unit = opponent_faction.player.choose_unit(eligible_units)
        elif len(eligible_units) == 1:
            target_unit = eligible_units[0]
        else:
            print(f"   No eligible target units.")
            return

        isDead = target_unit.damage_unit()

        if not isDead:
            target_unit.damage_unit()

class Command(SpecialAbility):
    def __init__(self):
        self.name = "Command"
        self.description = "Deal 1 rout (⚑ ). Then draw 1 Tactics card."

    def resolve(self, your_faction, opponent_faction):
        eligible_units = self.get_units_regular_rout_priority(opponent_faction)

        if len(eligible_units) > 1:
            target_unit = opponent_faction.player.choose_unit(eligible_units)
        elif len(eligible_units) == 1:
            target_unit = eligible_units[0]
        else:
            print(f"   No eligible target units.")
            return

        target_unit.rout_unit()

        your_faction.add_tactic_cards(1)

class LaySiege(SpecialAbility):
    def __init__(self):
        self.name = "Lay Siege"
        self.description = "Gain +2 Strength when determining the winner of this battle."

    def resolve(self, your_faction, opponent_faction):
        your_faction.add_strength(2)

class CrackShot(SpecialAbility):
    def __init__(self):
        self.name = "Crack Shot"
        self.description = "Deal 1 damage (◉ ) to the unit of your choice."

    def resolve(self, your_faction, opponent_faction):
        eligible_units = self.get_all_units(opponent_faction)

        if len(eligible_units) > 1:
            target_unit = your_faction.player.choose_unit(eligible_units)
        elif len(eligible_units) == 1:
            target_unit = eligible_units[0]
        else:
            print(f"   No eligible target units.")
            return

        target_unit.damage_unit()

class Charge(SpecialAbility):
    def __init__(self):
        self.name = "Charge"
        self.description = "Rout up to 2 enemy triangle (▲ ) units or 1 enemy rectangle (∎ ) unit of your choice."

    def resolve(self, your_faction, opponent_faction):
        eligible_units = self.get_standing_triangle_or_rectangle_units(opponent_faction)

        if len(eligible_units) > 1:
            target_unit = your_faction.player.choose_unit(eligible_units)
        elif len(eligible_units) == 1:
            target_unit = eligible_units[0]
        else:
            print(f"   No eligible target units.")
            return

        target_unit.rout_unit()

        if target_unit.unit_type.shape == "triangle":
            eligible_units = self.get_standing_triangle_units(opponent_faction)

            if len(eligible_units) > 1:
                target_unit = your_faction.player.choose_unit(eligible_units)
            elif len(eligible_units) == 1:
                target_unit = eligible_units[0]
            else:
                print(f"   No eligible target units.")
                return

            target_unit.rout_unit()

    def get_standing_triangle_or_rectangle_units(self, faction):
        # Gather all standing units
        eligible_units = [u for faction.unit_type in faction.unit_types for u in faction.unit_type.units if u.is_standing and (u.unit_type.shape == "triangle" or u.unit_type.shape == "rectangle")]

        return eligible_units

class WordOfVaal(SpecialAbility):
    def __init__(self):
        self.name = "Word of Vaal"
        self.description = "Your opponent must retreat 1 unit of your choice from the battle."

    def resolve(self, your_faction, opponent_faction):
        eligible_units = self.get_all_units(opponent_faction)

        if len(eligible_units) > 1:
            target_unit = your_faction.player.choose_unit(eligible_units)
        elif len(eligible_units) == 1:
            target_unit = eligible_units[0]
        else:
            print(f"   No eligible target units.")
            return

        target_unit.retreat_unit()

class Overpower(SpecialAbility):
    def __init__(self):
        self.name = "Overpower"
        self.description = "Deal 1 damage (◉ ) or destroy the damaged or routed enemy unit of your choice."

    def resolve(self, your_faction, opponent_faction):

        potential_regular_damage_targets = self.get_units_regular_damage_priority(opponent_faction)
        potential_damaged_or_routed_targets = self.get_all_damaged_and_routed_units(opponent_faction)

        if len(potential_regular_damage_targets) > 0 and len(potential_damaged_or_routed_targets) > 0:
            choice = your_faction.player.choose_option("Deal 1 damage (◉ )", "Destroy the damaged or routed enemy unit of your choice")
        elif len(potential_regular_damage_targets) > 0 and len(potential_damaged_or_routed_targets) == 0:
            choice = 1
        elif len(potential_regular_damage_targets) == 0 and len(potential_damaged_or_routed_targets) > 0:
            choice = 2
        else:
            print(f"   No eligible target units.")
            return

        if choice == 1:
            eligible_units = potential_regular_damage_targets

            if len(eligible_units) > 1:
                target_unit = opponent_faction.player.choose_unit(eligible_units)
            elif len(eligible_units) == 1:
                target_unit = eligible_units[0]
            else:
                print(f"   No eligible target units.")
                return

            target_unit.damage_unit()

        elif choice == 2:
            eligible_units = potential_damaged_or_routed_targets

            if len(eligible_units) > 1:
                target_unit = your_faction.player.choose_unit(eligible_units)
            elif len(eligible_units) == 1:
                target_unit = eligible_units[0]
            else:
                print(f"   No eligible target units.")
                return

            target_unit.destroy_unit()

    def get_all_damaged_and_routed_units(self, faction):
        # Gather all units
        eligible_units = [u for faction.unit_type in faction.unit_types for u in faction.unit_type.units if u.damage_taken > 0 or not u.is_standing]

        return eligible_units

class Undying(SpecialAbility):
    def __init__(self):
        self.name = "Undying"
        self.description = "Each of your Sorcerers have 2 health until the end of the battle."

    def resolve(self, your_faction, opponent_faction):

        your_sorcerer_unit_type = next((unit_type for unit_type in your_faction.unit_types if unit_type.name == "Sorcerer"), None)

        if your_sorcerer_unit_type != None:
            your_sorcerer_unit_type.health = 2

class Stun(SpecialAbility):
    def __init__(self):
        self.name = "Stun"
        self.description = "Your opponent must rout 1 of their units with initiative (🗲 ) 2 or higher."

    def resolve(self, your_faction, opponent_faction):
        eligible_units = self.get_unit_more_initiative_rout_priority(opponent_faction)

        if len(eligible_units) > 1:
            target_unit = opponent_faction.player.choose_unit(eligible_units)
        elif len(eligible_units) == 1:
            target_unit = eligible_units[0]
        else:
            print(f"   No eligible target units.")
            return

        target_unit.rout_unit()

    def get_unit_more_initiative_rout_priority(self, faction):
        # Gather all units
        all_units = [u for faction.unit_type in faction.unit_types for u in faction.unit_type.units]
        # Sort units according to priority
        standing_undamaged_units_with_high_initiative = [u for u in all_units if u.is_standing and u.damage_taken == 0 and u.unit_type.initiative > 1]
        standing_damaged_units_with_high_initiative = [u for u in all_units if u.is_standing and u.damage_taken > 0 and u.unit_type.initiative > 1]
        standing_undamaged_units_with_low_initiative = [u for u in all_units if u.is_standing and u.damage_taken == 0 and u.unit_type.initiative == 1]
        standing_damaged_units_with_low_initiative = [u for u in all_units if u.is_standing and u.damage_taken > 0 and u.unit_type.initiative == 1]

        if standing_undamaged_units_with_high_initiative:
            eligible_units = standing_undamaged_units_with_high_initiative
        elif standing_damaged_units_with_high_initiative:
            eligible_units = standing_damaged_units_with_high_initiative
        elif standing_undamaged_units_with_low_initiative:
            eligible_units = standing_undamaged_units_with_low_initiative
        elif standing_damaged_units_with_low_initiative:
            eligible_units = standing_damaged_units_with_low_initiative
        else:
            eligible_units = []

        return eligible_units

class Ravage(SpecialAbility):
    def __init__(self):
        self.name = "Ravage"
        self.description = "Deal 1 damage (◉ ) and then draw and resolve a new Fate cards (limit once per beastman)."

    def resolve(self, your_faction, opponent_faction):
        eligible_units = self.get_units_regular_damage_priority(opponent_faction)

        if len(eligible_units) > 1:
            target_unit = opponent_faction.player.choose_unit(eligible_units)
        elif len(eligible_units) == 1:
            target_unit = eligible_units[0]
        else:
            print(f"   No eligible target units.")
            return

        target_unit.damage_unit()

        # Make a workaround so that I don't have to import the Fate Deck to this class,
        # the distribution is the same.
        draw_card = random.randint(1, 31)

        if draw_card <= 14:
            print(f"   Fate card result: deal 1 damage (◉ )")
            eligible_units = self.get_units_regular_damage_priority(opponent_faction)
            if len(eligible_units) > 1:
                target_unit = opponent_faction.player.choose_unit(eligible_units)
            elif len(eligible_units) == 1:
                target_unit = eligible_units[0]
            else:
                print(f"   No eligible target units.")
                return
            target_unit.damage_unit()

        elif draw_card > 14 and draw_card <= 18:
            print(f"   Fate card result: deal 1 rout (⚑ )")
            eligible_units = self.get_units_regular_rout_priority(opponent_faction)
            if len(eligible_units) > 1:
                target_unit = opponent_faction.player.choose_unit(eligible_units)
            elif len(eligible_units) == 1:
                target_unit = eligible_units[0]
            else:
                print(f"   No eligible target units.")
                return
            target_unit.rout_unit()

class Burning(SpecialAbility):
    def __init__(self):
        self.name = "Burning"
        self.description = "Your opponent must deal 1 damage (◉ ) to 2 of their different standing units."

    def resolve(self, your_faction, opponent_faction):
        eligible_units = self.get_standing_damaged_units(opponent_faction)

        first_target_unit = None
        second_target_unit = None

        if len(eligible_units) > 3:
            first_target_unit, second_target_unit = opponent_faction.player.choose_two_units(eligible_units)
        elif len(eligible_units) == 2:
            first_target_unit = eligible_units[0]
            second_target_unit = eligible_units[1]
        elif len(eligible_units) == 1:
            first_target_unit = eligible_units[0]
            eligible_units = self.get_standing_undamaged_units(opponent_faction)
            if len(eligible_units) > 2:
                second_target_unit = opponent_faction.player.choose_unit(eligible_units)
            elif len(eligible_units) == 1:
                second_target_unit = eligible_units[0]
            else:
                print(f"   Only one eligible target unit.")
        else:
            eligible_units = self.get_standing_undamaged_units(opponent_faction)
            if len(eligible_units) > 3:
                first_target_unit, second_target_unit = opponent_faction.player.choose_two_units(eligible_units)
            elif len(eligible_units) == 2:
                first_target_unit = eligible_units[0]
                second_target_unit = eligible_units[1]
            elif len(eligible_units) == 1:
                first_target_unit = eligible_units[0]
                print(f"   Only one eligible target unit.")
            else:
                print(f"   No eligible target units.")
                return

        if first_target_unit != None:
            first_target_unit.damage_unit()

        if second_target_unit != None:
            second_target_unit.damage_unit()

    def get_standing_damaged_units(self, faction):
        all_units = [u for faction.unit_type in faction.unit_types for u in faction.unit_type.units]

        eligible_units = [u for u in all_units if u.is_standing and u.damage_taken > 0]

        return eligible_units

    def get_standing_undamaged_units(self, faction):
        all_units = [u for faction.unit_type in faction.unit_types for u in faction.unit_type.units]

        eligible_units = [u for u in all_units if u.is_standing and u.damage_taken == 0]

        return eligible_units

class FlamingBreath(SpecialAbility):
    def __init__(self):
        self.name = "Flaming Breath"
        self.description = "Destroy up to 3 enemy triangle (▲ ) units of your choice."

    def resolve(self, your_faction, opponent_faction):
        for i in range(3):
            eligible_units = self.get_standing_triangle_units(opponent_faction)

            if len(eligible_units) > 1:
                target_unit = your_faction.player.choose_unit(eligible_units)
            elif len(eligible_units) == 1:
                target_unit = eligible_units[0]
            else:
                print(f"   No eligible target units.")
                return

            target_unit.destroy_unit()

class Rage(SpecialAbility):
    def __init__(self):
        self.name = "Rage"
        self.description = "Deal 1 damage (◉ ) for each damage on 1 of your Giants."

    def resolve(self, your_faction, opponent_faction):

        # Filter out your giants
        your_giant_units = [unit for unit in your_faction.unit_type.units if unit.unit_type.name == "Giant"]

        if not your_giant_units:
            max_number_of_damage_taken = 0
        else:
            max_number_of_damage_taken = max(unit.damage_taken for unit in your_giant_units)

        for i in range(max_number_of_damage_taken):
            eligible_units = self.get_units_regular_damage_priority(opponent_faction)

            if len(eligible_units) > 1:
                target_unit = opponent_faction.player.choose_unit(eligible_units)
            elif len(eligible_units) == 1:
                target_unit = eligible_units[0]
            else:
                print(f"   No eligible target units.")
                return

            target_unit.damage_unit()