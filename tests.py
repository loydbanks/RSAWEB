import unittest
from check_poker_hand import PokerGame

game = PokerGame()
class TestPockerHandsApp(unittest.TestCase):
    def test_check_hand_is_valid(self):
        self.assertEqual(game.check_if_hand_is_valid(['JC', 'TC', '9C', '8C', '7C']), "")
        self.assertEqual(game.check_if_hand_is_valid(['JC', '10C', '9d', '8C', '7C']),
                        "A wrong card has been given in your input. Please make sure you have inserted correct card and suit")

    def test_flush(self):
        self.assertEqual(game.flush_hand_evaluation(['JD', '9D', '8D', '4D', '3D']), "Flush")

    def test_five_of_kind(self):
        self.assertEqual(game.five_of_a_kind_evaluation(['AS', 'AD', 'AC', 'AH', 'JD']), "Five of a kind")
    
    def test_four_of_kind(self):
        self.assertEqual(game.four_of_a_kind_evaluation(['5S', '5D', '5C', '5H', '2D']), "Four of a kind")