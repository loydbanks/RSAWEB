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

    # This function checks that a poker hand is 'five of a kind' rank
    def five_of_a_kind_evaluation(self, hand):
        values = [v[0] for v in hand]
        card_values = [self.card_order_dict[i] for i in values]
        """
        We check to see if we have all 4 of the 5 cards as the same and if if we have a wild card
        Use an array which has [True, True, True, False] and that shows us not all 4 elements are the same and
        this can't be a five of a kind hand. We also check if value of the last card is greater than or equal 11 making
        it a wildcard, if both are satisfied, we have Five of a kind       
        """
        if [element == card_values[0] for element in card_values[:4]][0] is True and sorted(card_values)[-1] >=11:
            return "Five of a kind"
        return ""
    
    # This function checks if pocker hand is 'four of a kind' rank
    def four_of_a_kind_evaluation(self, hand):
        values = [i[0] for i in hand]
        suits = [suit[1] for suit in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        # We check if 4 of the 5 cards are the same then the last card is just any card(aside from wildcard)
        if sorted([element == suits[0] for element in suits[:5]])[:4] and sorted(value_counts.values()) == [1, 4]:
            return "Four of a kind"
        return ""
    
    # This function checks that we have a 'straight' poker hand rank 
    def straight_hand_evaluation(self, hand):
        card_numbers = [card[0] for card in hand] # This array is to keep all the card numbers
        count_cards_in_hand = defaultdict(lambda:0) # This dictionary will help count the cards we have
        card_rank_values = [self.card_order_dict[i] for i in card_numbers] # This array helps us get the rankings of each card in numbers

        """
        Saw a pattern emerge when we minus highest card and lowest card and that's we always get a 4 or 9
        so we minus the highest card from lowest card 
        """
        card_range = max(list(sorted(card_rank_values))) - min(list(sorted(card_rank_values)))

        for card in card_numbers:
            count_cards_in_hand[card]+=1
        """
        We check that card numbers to do not repeat and that we either get a 4 or 9 when we subtract highest card from loweest
        and use these as conditions for determining a 'Straight' hand rank
        """
        if len(set(count_cards_in_hand.values())) == 1 and (card_range == 4 or card_range == 9):
            return "Straight"
        return ""

    # This function check if a list has in descending order and the difference between the elements is '1'
    def has_stepsize_one(self, it):
        return all(x1 - x2 == 1 for x1, x2 in zip(it[:-1], it[1:]))

    # This function checks for a 'straight flush' given a poker hand
    def straight_flush_evaluation(self, hand):
        values = [v[0] for v in hand]
        suits = [s[1] for s in hand]
        card_values = [self.card_order_dict[i] for i in values]
        sorted_cards = sorted(card_values, reverse=True)
        # We check that each of the cards are in descending order witha difference of one and all the suits of the cards are the same 
        if self.has_stepsize_one(sorted_cards) and all(card == suits[0] for card in suits) is True:
            return "Straight Flush"
        return ""

    # This function checks if the given poker hand is a 'Full house'
    def full_house_evaluation(self, hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        """
        We check if 3 cards are the same and the other 2 are not, the loop above will do the counting for us and we
        use the values() function and sorted() function to show we 2 cards not the same and 3 are the same 
        """
        if sorted(value_counts.values()) == [2,3]:
            return "Full house"
        return ""

    # The function below determines if a poker hand is three of a kind or not
    def three_of_a_kind_evaluation(self, hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        """
        We use the loop above to count for us so we can determine how many cards are the same and how many are not
        and we get that 3 cards are of the same number and 2 cards are not of the same number, hence 'Three of a kind' 
        """
        if list(value_counts.values()) == [3, 1, 1]:
            return "Three of a kind"
        return ""

    # This function is used to check if poker hand is 'Two pairs' rank
    def two_pairs_evaluation(self, hand):
        values = [v[0] for v in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        """
        We use the loop above to count the same occurrence of card numbers and 
        use get that we have 2 pairs of matching numbers hence 'Two pair' hand rank
        """
        if sorted(value_counts.values()) == [1, 2, 2]:
            return "Two pair"
        return ""

    # We use the function below to get if a poker hand is 'One pair'
    def one_pair_evaluation(self, hand):
        values = [v[0] for v in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values()) == [1, 1, 1, 2]:
            return "One pair"
        return ""