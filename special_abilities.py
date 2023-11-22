class SpecialAbility:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def resolve(self, your_faction, opponent_faction):
        raise NotImplementedError

class RegularDamage(SpecialAbility):
    def __init__(self):
        self.name = "Damage"
        self.description = "Deal 1 damage (◉ )."

    def resolve(self, your_faction, opponent_faction):
        target_units = self.get_units_regular_damage_priority(opponent_faction)

        if len(target_units) > 1:
            target_unit = opponent_faction.player.choose_unit(target_units)
        elif len(target_units) == 1:
            target_unit = target_units[0]
        else:
            print(f"   No eligible target untis.")
            return

        target_unit.damage_unit()

    def get_units_regular_damage_priority(self, faction):
        all_units = [u for faction.unit_type in faction.unit_types for u in faction.unit_type.units]

        damaged_units = [u for u in all_units if u.damage_taken > 0]
        standing_units = [u for u in all_units if u.is_standing and u.damage_taken == 0]
        routed_units = [u for u in all_units if not u.is_standing]

        if damaged_units:
            target_units = damaged_units
        elif standing_units:
            target_units = standing_units
        elif routed_units:
            target_units = routed_units
        else:
            target_units = []

        return target_units

class RegularRout(SpecialAbility):
    def __init__(self):
        self.name = "Rout"
        self.description = "Deal 1 rout (⚑ )."

    def resolve(self, your_faction, opponent_faction):
        target_units = self.get_units_regular_rout_priority(opponent_faction)

        if len(target_units) > 1:
            target_unit = opponent_faction.player.choose_unit(target_units)
        elif len(target_units) == 1:
            target_unit = target_units[0]
        else:
            print(f"   No eligible target untis.")
            return

        target_unit.rout_unit()

    def get_units_regular_rout_priority(self, faction):
        # Gather all standing units
        standing_units = [u for faction.unit_type in faction.unit_types for u in faction.unit_type.units if u.is_standing]

        # Sort units according to priority: first undamaged standing units, then damaged standing units
        undamaged_standing_units = [u for u in standing_units if u.damage_taken == 0]
        damaged_standing_units = [u for u in standing_units if u.damage_taken > 0]

        if undamaged_standing_units:
            target_units = undamaged_standing_units
        elif damaged_standing_units:
            target_units = damaged_standing_units
        else:
            target_units = []

        return target_units

class ConcentratedFire(SpecialAbility):
    def __init__(self):
        self.name = "Concentrated Fire"
        self.description = "Deal 1 damage (◉ ). Your opponent must assign this to a unit with more than 1 health (♥), if able."

    def resolve(self, your_faction, opponent_faction):
        target_units = self.get_unit_more_health_damage_priority(opponent_faction)

        if len(target_units) > 1:
            target_unit = opponent_faction.player.choose_unit(target_units)
        elif len(target_units) == 1:
            target_unit = target_units[0]
        else:
            print(f"   No eligible target untis.")
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
            target_units = damaged_units
        elif standing_units_with_high_health:
            target_units = standing_units_with_high_health
        elif standing_units_with_low_health:
            target_units = standing_units_with_low_health
        elif routed_units_with_high_health:
            target_units = routed_units_with_high_health
        elif routed_units_with_low_health:
            target_units = routed_units_with_low_health
        else:
            target_units = []

        return target_units
