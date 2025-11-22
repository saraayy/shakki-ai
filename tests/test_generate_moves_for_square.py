import unittest
from shakki_ai.board import Board

class TestGenerateMovesForSquare(unittest.TestCase):
    def setUp(self):
        self.b = Board()

    def test_empty_square_returns_empty_list(self):
        moves = self.b.generate_moves_for_square(4,4)
        self.assertEqual(moves, [])


    def test_wrong_color_piece_returns_empty_list(self):
        moves = self.b.generate_moves_for_square(0,0)
        self.assertEqual(moves, [])