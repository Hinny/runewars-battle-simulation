import random

class FateCard:
    def __init__(self, card_id, result_triangle, result_circle, result_rectangle, result_hexagon):
        self.card_id = card_id
        self.result = {
            "triangle": result_triangle,
            "circle": result_circle,
            "rectangle": result_rectangle,
            "hexagon": result_hexagon
        }

    def __str__(self):
        return f"Fate Card {self.card_id}"

class FateDeck:
    def __init__(self):
        self.draw_pile = []
        self.drawn_cards = []
        self.discard_pile = []

        for card_id in range(1, 31):
            fate_card = FateCard(card_id, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
            self.draw_pile.append(fate_card)

        # Legend:
        # (2, 0, 0) = 2 Damage
        # (0, 1, 0) = 1 rout
        # (0, 0, 1) = 1 orb

        self.draw_pile[0].result["triangle"] = (0, 0, 0)
        self.draw_pile[0].result["circle"] = (0, 0, 1)
        self.draw_pile[0].result["rectangle"] = (0, 2, 0)
        self.draw_pile[0].result["hexagon"] = (2, 0, 0)

        self.draw_pile[1].result["triangle"] = (0, 0, 0)
        self.draw_pile[1].result["circle"] = (0, 0, 1)
        self.draw_pile[1].result["rectangle"] = (0, 2, 0)
        self.draw_pile[1].result["hexagon"] = (1, 0, 0)

        self.draw_pile[2].result["triangle"] = (0, 0, 0)
        self.draw_pile[2].result["circle"] = (0, 0, 1)
        self.draw_pile[2].result["rectangle"] = (0, 0, 1)
        self.draw_pile[2].result["hexagon"] = (1, 0, 0)

        self.draw_pile[3].result["triangle"] = (0, 0, 0)
        self.draw_pile[3].result["circle"] = (0, 0, 1)
        self.draw_pile[3].result["rectangle"] = (0, 0, 1)
        self.draw_pile[3].result["hexagon"] = (0, 0, 0)

        self.draw_pile[4].result["triangle"] = (0, 1, 0)
        self.draw_pile[4].result["circle"] = (1, 0, 0)
        self.draw_pile[4].result["rectangle"] = (0, 0, 0)
        self.draw_pile[4].result["hexagon"] = (0, 0, 0)

        self.draw_pile[5].result["triangle"] = (0, 1, 0)
        self.draw_pile[5].result["circle"] = (1, 0, 0)
        self.draw_pile[5].result["rectangle"] = (0, 0, 0)
        self.draw_pile[5].result["hexagon"] = (0, 0, 1)

        self.draw_pile[6].result["triangle"] = (0, 1, 0)
        self.draw_pile[6].result["circle"] = (0, 0, 0)
        self.draw_pile[6].result["rectangle"] = (0, 0, 0)
        self.draw_pile[6].result["hexagon"] = (0, 0, 1)

        self.draw_pile[7].result["triangle"] = (0, 1, 0)
        self.draw_pile[7].result["circle"] = (0, 0, 0)
        self.draw_pile[7].result["rectangle"] = (0, 1, 0)
        self.draw_pile[7].result["hexagon"] = (3, 0, 0)

        self.draw_pile[8].result["triangle"] = (0, 0, 1)
        self.draw_pile[8].result["circle"] = (0, 0, 0)
        self.draw_pile[8].result["rectangle"] = (0, 1, 0)
        self.draw_pile[8].result["hexagon"] = (3, 0, 0)

        self.draw_pile[9].result["triangle"] = (0, 0, 1)
        self.draw_pile[9].result["circle"] = (0, 0, 0)
        self.draw_pile[9].result["rectangle"] = (0, 1, 0)
        self.draw_pile[9].result["hexagon"] = (2, 0, 0)

        self.draw_pile[10].result["triangle"] = (0, 0, 0)
        self.draw_pile[10].result["circle"] = (0, 0, 1)
        self.draw_pile[10].result["rectangle"] = (2, 0, 0)
        self.draw_pile[10].result["hexagon"] = (2, 0, 0)

        self.draw_pile[11].result["triangle"] = (0, 0, 0)
        self.draw_pile[11].result["circle"] = (0, 0, 1)
        self.draw_pile[11].result["rectangle"] = (2, 0, 0)
        self.draw_pile[11].result["hexagon"] = (1, 0, 0)

        self.draw_pile[12].result["triangle"] = (0, 0, 0)
        self.draw_pile[12].result["circle"] = (0, 0, 1)
        self.draw_pile[12].result["rectangle"] = (0, 0, 1)
        self.draw_pile[12].result["hexagon"] = (1, 0, 0)

        self.draw_pile[13].result["triangle"] = (0, 0, 0)
        self.draw_pile[13].result["circle"] = (0, 0, 1)
        self.draw_pile[13].result["rectangle"] = (0, 0, 1)
        self.draw_pile[13].result["hexagon"] = (1, 0, 0)

        self.draw_pile[14].result["triangle"] = (1, 0, 0)
        self.draw_pile[14].result["circle"] = (0, 1, 0)
        self.draw_pile[14].result["rectangle"] = (0, 0, 0)
        self.draw_pile[14].result["hexagon"] = (0, 0, 0)

        self.draw_pile[15].result["triangle"] = (1, 0, 0)
        self.draw_pile[15].result["circle"] = (0, 1, 0)
        self.draw_pile[15].result["rectangle"] = (0, 0, 0)
        self.draw_pile[15].result["hexagon"] = (0, 0, 1)

        self.draw_pile[16].result["triangle"] = (1, 0, 0)
        self.draw_pile[16].result["circle"] = (0, 0, 0)
        self.draw_pile[16].result["rectangle"] = (0, 0, 0)
        self.draw_pile[16].result["hexagon"] = (0, 0, 1)

        self.draw_pile[17].result["triangle"] = (1, 0, 0)
        self.draw_pile[17].result["circle"] = (0, 0, 0)
        self.draw_pile[17].result["rectangle"] = (1, 0, 0)
        self.draw_pile[17].result["hexagon"] = (3, 0, 0)

        self.draw_pile[18].result["triangle"] = (0, 0, 1)
        self.draw_pile[18].result["circle"] = (0, 0, 0)
        self.draw_pile[18].result["rectangle"] = (1, 0, 0)
        self.draw_pile[18].result["hexagon"] = (0, 0, 0)

        self.draw_pile[19].result["triangle"] = (0, 0, 1)
        self.draw_pile[19].result["circle"] = (0, 0, 0)
        self.draw_pile[19].result["rectangle"] = (1, 0, 0)
        self.draw_pile[19].result["hexagon"] = (2, 0, 0)

        self.draw_pile[20].result["triangle"] = (0, 0, 0)
        self.draw_pile[20].result["circle"] = (0, 0, 1)
        self.draw_pile[20].result["rectangle"] = (2, 0, 0)
        self.draw_pile[20].result["hexagon"] = (0, 2, 0)

        self.draw_pile[21].result["triangle"] = (0, 0, 0)
        self.draw_pile[21].result["circle"] = (0, 0, 1)
        self.draw_pile[21].result["rectangle"] = (2, 0, 0)
        self.draw_pile[21].result["hexagon"] = (0, 2, 0)

        self.draw_pile[22].result["triangle"] = (0, 0, 0)
        self.draw_pile[22].result["circle"] = (0, 0, 1)
        self.draw_pile[22].result["rectangle"] = (0, 0, 1)
        self.draw_pile[22].result["hexagon"] = (0, 1, 0)

        self.draw_pile[23].result["triangle"] = (0, 0, 0)
        self.draw_pile[23].result["circle"] = (0, 0, 1)
        self.draw_pile[23].result["rectangle"] = (0, 0, 1)
        self.draw_pile[23].result["hexagon"] = (0, 0, 0)

        self.draw_pile[24].result["triangle"] = (1, 0, 0)
        self.draw_pile[24].result["circle"] = (1, 0, 0)
        self.draw_pile[24].result["rectangle"] = (0, 0, 0)
        self.draw_pile[24].result["hexagon"] = (0, 0, 0)

        self.draw_pile[25].result["triangle"] = (1, 0, 0)
        self.draw_pile[25].result["circle"] = (1, 0, 0)
        self.draw_pile[25].result["rectangle"] = (0, 0, 0)
        self.draw_pile[25].result["hexagon"] = (0, 0, 1)

        self.draw_pile[26].result["triangle"] = (1, 0, 0)
        self.draw_pile[26].result["circle"] = (0, 0, 0)
        self.draw_pile[26].result["rectangle"] = (0, 0, 0)
        self.draw_pile[26].result["hexagon"] = (0, 0, 1)

        self.draw_pile[27].result["triangle"] = (1, 0, 0)
        self.draw_pile[27].result["circle"] = (0, 0, 0)
        self.draw_pile[27].result["rectangle"] = (1, 0, 0)
        self.draw_pile[27].result["hexagon"] = (0, 2, 0)

        self.draw_pile[28].result["triangle"] = (0, 0, 1)
        self.draw_pile[28].result["circle"] = (0, 0, 0)
        self.draw_pile[28].result["rectangle"] = (1, 0, 0)
        self.draw_pile[28].result["hexagon"] = (0, 2, 0)

        self.draw_pile[29].result["triangle"] = (0, 0, 1)
        self.draw_pile[29].result["circle"] = (0, 0, 0)
        self.draw_pile[29].result["rectangle"] = (1, 0, 0)
        self.draw_pile[29].result["hexagon"] = (0, 2, 0)

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.draw_pile)

    def draw_hand(self, num_cards):
        hand = []

        for _ in range(0, num_cards):
            card = self.draw_card()
            hand.append(card)

        return hand

    def draw_card(self):
        if not self.draw_pile:
            # If draw pile is empty, shuffle the discard pile becomming the new draw pile
            self.draw_pile.extend(self.discard_pile)
            self.discard_pile = []
            self.shuffle()

        card = self.draw_pile.pop()
        self.drawn_cards.append(card)

        return card

    def discard_hand(self, cards):
        self.discard_pile.extend(cards)
        for card in cards:
            self.drawn_cards.remove(card)

    def calculate_total_results(self, cards, shape):
        total_damage = 0
        total_rout = 0
        total_orb = 0

        for card in cards:
            result = card.result[shape]
            total_damage += result[0]
            total_rout += result[1]
            total_orb += result[2]
        return total_damage, total_rout, total_orb
    