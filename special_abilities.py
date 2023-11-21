class SpecialAbility:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def resolve(self):
        raise NotImplementedError

class RegularDamage(SpecialAbility):
    def __init__(self):
        self.name = "Damage"
        self.description = "Deal 1 damage (◉ )."
    
    def resolve(self, your_faction, opponent_faction):
        print(f"{self.description}")


class RegularRout(SpecialAbility):
    def __init__(self):
        self.name = "Rout"
        self.description = "Deal 1 rout (⚑ )."
    
    def resolve(self, your_faction, opponent_faction):
        print(f"{self.description}")


class ConcentratedFire(SpecialAbility):
    def __init__(self):
        self.name = "Concentrated Fire"
        self.description = "Deal 1 damage (◉ ). Your opponent must assign this to a unit with more than 1 health (♥), if able."
    
    def resolve(self, your_faction, opponent_faction):
        print(f"{self.description}")

class PlaceHolder(SpecialAbility):
    def __init__(self):
        self.name = "Placeholder"
        self.description = "Placeholder"
    
    def resolve(self, your_faction, opponent_faction):
        pass

    def deal_damage(self, number_of_damage):
        """
        Deal the number of damage to units in this faction, using this priority according to the rules:
        1. Already damaged units (regardless if they are standing or routed).
        2. Undamaged standing units.
        3. Routed units.
        If a units total damage taken is equal to its health, it will be destroyed (and removed from the faction).
        """
        print(" - Dealing " + str(number_of_damage) + " damage to " + self.name + " unit(s)")
        for _ in range(number_of_damage):
            # Gather all units
            all_units = [u for unit_type in self.unit_types for u in unit_type.units]
            # Sort units according to priority: first damaged, then standing, then routed
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
                # No units left to take damage
                break

            # Assign damage to the first target unit
            target_unit = self.player.choose_own_unit_for_regular_damage(target_units)
            print("   " + target_unit.unit_type.name + " takes 1 damage")
            target_unit.damage_taken += 1
            # Check if the unit is destroyed
            if target_unit.damage_taken >= target_unit.unit_type.health:
                print("   (" + target_unit.unit_type.name + " destroyed)")
                target_unit.unit_type.units.remove(target_unit)

    def deal_rout(self, number_of_rout):
        """
        Routs the number of units in this faction, using this priority according to the rules:
        1. Undamaged standing units
        2. Damaged standing units.
        Units can only be routed when standing.
        If there are not more standing units, no more can be routed.
        """
        print(" - Routing " + str(number_of_rout) + " " + self.name + " unit(s)")
        for _ in range(number_of_rout):
            # Gather all standing units
            standing_units = [u for unit_type in self.unit_types for u in unit_type.units if u.is_standing]
            # Sort units according to priority: first undamaged standing units, then damaged standing units
            undamaged_standing_units = [u for u in standing_units if u.damage_taken == 0]
            damaged_standing_units = [u for u in standing_units if u.damage_taken > 0]

            # Append the lists in priority order
            target_units = undamaged_standing_units + damaged_standing_units

            if undamaged_standing_units:
                target_units = undamaged_standing_units
            elif damaged_standing_units:
                target_units = damaged_standing_units
            else:
                # No more standing units to rout
                break

            target_unit = self.player.choose_own_unit_for_regular_rout(target_units)
            print("   " + target_unit.unit_type.name + " is routed")
            target_unit.is_standing = False
