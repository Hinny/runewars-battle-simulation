import random
from fate_deck import FateDeck
from factions import Faction
from units import UnitType, Unit

class BattleSimulator:
    def __init__(self, attacker_faction, defender_faction, fate_deck):
        self.attacker_faction = attacker_faction
        self.defender_faction = defender_faction
        self.fate_deck = fate_deck

    def simulate_round(self):
        # Organisera attackerarens enheter efter initiativ
        attacker_unit_types_by_initiative = {}
        for unit_type in self.attacker_faction.unit_types:
            initiative = unit_type.initiative
            if initiative not in attacker_unit_types_by_initiative:
                attacker_unit_types_by_initiative[initiative] = []
            attacker_unit_types_by_initiative[initiative].append(unit_type)

        # Organisera försvararens enheter efter initiativ
        defender_unit_types_by_initiative = {}
        for unit_type in self.defender_faction.unit_types:
            initiative = unit_type.initiative
            if initiative not in defender_unit_types_by_initiative:
                defender_unit_types_by_initiative[initiative] = []
            defender_unit_types_by_initiative[initiative].append(unit_type)

        # Loopa igenom initiativen och välj enhetstyper
        for initiative in range(1, 6):

            more_units_to_activate = True

            while more_units_to_activate:
                # Sortera ut unit_types som har minst en stående (isStanding) och inte aktiverad (hasActivated) enhet och som också tillhör detta initiativet
                standing_not_activated_attacker_unit_types = [
                    unit_type for unit_type in self.attacker_faction.unit_types
                    if unit_type.initiative == initiative and 
                    any(unit.isStanding and not unit.hasActivated for unit in unit_type.units)
                ]

                standing_not_activated_defender_unit_types = [
                    unit_type for unit_type in self.defender_faction.unit_types
                    if unit_type.initiative == initiative and 
                    any(unit.isStanding and not unit.hasActivated for unit in unit_type.units)
                ]

                # Slumpmässigt välj enhetstyper om de finns tillgängliga
                if standing_not_activated_attacker_unit_types:
                    attacker_unit_type_choice = random.choice(standing_not_activated_attacker_unit_types)
                else:
                    attacker_unit_type_choice = None

                if standing_not_activated_defender_unit_types:
                    defender_unit_type_choice = random.choice(standing_not_activated_defender_unit_types)
                else:
                    defender_unit_type_choice = None

                # Om åtminstone en attackerande eller försvarande enhetstyp valdes, utför sub-steg
                if attacker_unit_type_choice or defender_unit_type_choice:
                    self.perform_sub_step(attacker_unit_type_choice, defender_unit_type_choice)
                else:
                    more_units_to_activate = False

    def perform_sub_step(self, attacker_unit_type, defender_unit_type):
        attacker_damage = 0
        attacker_rout = 0
        attacker_orb = 0
        defender_damage = 0
        defender_rout = 0
        defender_orb = 0

        if attacker_unit_type:
            attacker_hand = self.fate_deck.draw_hand(len(attacker_unit_type.units))
            (attacker_damage, attacker_rout, attacker_orb) = self.fate_deck.calculate_total_results(attacker_hand, attacker_unit_type.shape)
        if defender_unit_type:
            defender_hand = self.fate_deck.draw_hand(len(defender_unit_type.units))
            (defender_damage, defender_rout, defender_orb) = self.fate_deck.calculate_total_results(defender_hand, defender_unit_type.shape)

        for _ in range(0, attacker_orb):
                    print("Performing " + attacker_unit_type.special_ability) #TODO: replace with actual ability

        for _ in range(0, defender_orb):
            print("Performing " + defender_unit_type.special_ability) #TODO: replace with actual ability

        if (attacker_damage > 0):
            self.defender_faction.deal_damage(attacker_damage)
        if (defender_damage > 0):
            self.attacker_faction.deal_damage(defender_damage)

        if (attacker_rout > 0):
            self.defender_faction.deal_rout(attacker_rout)
        if (defender_rout > 0):
            self.attacker_faction.deal_rout(defender_rout)

        if attacker_unit_type:
            for unit in attacker_unit_type.units:
                unit.hasActivated = True
            self.fate_deck.discard_hand(attacker_hand)
        
        if defender_unit_type:
            for unit in defender_unit_type.units:
                unit.hasActivated = True
            self.fate_deck.discard_hand(defender_hand)
