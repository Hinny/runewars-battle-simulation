class Faction:
    def __init__(self, name):
        self.name = name
        self.unit_types = []

    def add_unit_type(self, unit_type):
        self.unit_types.append(unit_type)

    def deal_damage(self, number_of_damage):
        """
        Deal the number of damage to units in this faction, using this priority according to the rules:
        1. Already damaged units (regardless if they are standing or routed).
        2. Undamaged standing units.
        3. Routed units.
        If a units total damage taken is equal to its health, it will be destroyed (and removed from the faction).
        """
        for _ in range(number_of_damage):
            # Gather all units
            all_units = [u for unit_type in self.unit_types for u in unit_type.units]
            # Sort units according to priority: first damaged, then standing, then routed
            damaged_units = [u for u in all_units if u.damage_taken > 0]
            standing_units = [u for u in all_units if u.is_standing and u.damage_taken == 0]
            routed_units = [u for u in all_units if not u.is_standing]

            # Append the lists in priority order
            target_units = damaged_units + standing_units + routed_units

            if target_units:
                # Assign damage to the first target unit
                target_unit = target_units[0]
                print(" - Dealing 1 damage to " + self.name + " " + target_unit.unit_type.name)
                target_unit.damage_taken += 1
                # Check if the unit is destroyed
                if target_unit.damage_taken >= target_unit.unit_type.health:
                    print("   (" + target_unit.unit_type.name + " destroyed)")
                    target_unit.unit_type.units.remove(target_unit)
            else:
                # No units left to take damage
                break

    def deal_rout(self, number_of_rout):
        """
        Routs the number of units in this faction, using this priority according to the rules:
        1. Undamaged standing units
        2. Damaged standing units.
        Units can only be routed when standing.
        If there are not more standing units, no more can be routed.
        """
        for _ in range(number_of_rout):
            # Gather all standing units
            standing_units = [u for unit_type in self.unit_types for u in unit_type.units if u.is_standing]
            # Sort units according to priority: first undamaged standing units, then damaged standing units
            undamaged_standing_units = [u for u in standing_units if u.damage_taken == 0]
            damaged_standing_units = [u for u in standing_units if u.damage_taken > 0]

            # Append the lists in priority order
            target_units = undamaged_standing_units + damaged_standing_units

            if target_units:
                # Rout the first target unit
                target_unit = target_units[0]
                print(" - Routing " + self.name + " " + target_unit.unit_type.name)
                target_unit.is_standing = False
            else:
                # No more standing units to rout
                break

