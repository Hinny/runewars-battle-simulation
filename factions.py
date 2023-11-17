class Faction:
    def __init__(self, name):
        self.name = name
        self.unit_types = []

    def add_unit_type(self, unit_type):
        self.unit_types.append(unit_type)

    def deal_damage(self, number_of_damage):
        print("Dealing " + str(number_of_damage) + " damage") #TODO: replace with actual ability

    def deal_rout(self, number_of_rout):
        print("Routing " + str(number_of_rout) + " unit(s)") #TODO: replace with actual ability
