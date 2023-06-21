from collections import defaultdict

"""
for the 10 card, please use T
for the Joker card, please use J
for the QUEEN card please use Q
for the KING card please use K
for the ACE card please use A
"""


class PokerGame:
    card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}
    suits_for_cards = {'S': 'Spades', 'C': 'Clubs', 'H': 'Hearts', 'D': 'Diamonds'}

    # This is where we get the input from user
    def get_poker_hand(self):
        cards = []
        print("Pease give input in the form of TS, 4D, 5C etc")
        for card_number in range(1, 6):
            prompt = input("Please add card {}:\n".format(card_number))
            cards.append(prompt)
        return cards

    # We check if the given poker hand is valid. Example 4D is valid but 10D is not, use T for 10
    def check_if_hand_is_valid(self, hand):
        card_suits = [h[1] for h in hand]
        cards = [card[0] for card in hand]
        for suit in card_suits:
            for card in cards:
                if suit not in list(self.suits_for_cards.keys()) or card not in list(self.card_order_dict.keys()):
                    return "A wrong card has been given in your input. Please make sure you have inserted correct card and suit"
        return ""

    # This function checks if a poker hand is flush ranking
    def flush_hand_evaluation(self, hand):
        suits = [h[1] for h in hand]
        # we use check if it is equal to 1 because all cards have the same suit
        if len(set(suits)) == 1:
            return "Flush"
        return ""