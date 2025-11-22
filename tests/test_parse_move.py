import unittest
from shakki_ai.board import Board

class TestParseMove(unittest.TestCase):
    def setUp(self):
        self.b = Board()

    def test_parse_move_e2e4(self):
        move = self.b.parse_move("e2e4")

        self.assertEqual(move, ((6,4), (4,4)))

    def test_parse_move_b1c3(self):
        move = self.b.parse_move("b1c3")

        self.assertEqual(move, ((7,1),(5,2)))

