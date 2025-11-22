import unittest
from shakki_ai.board import Board

class TestKnightMoves(unittest.TestCase):
    def setUp(self):
        self.b = Board()
    
    def test_knight_in_the_middle(self):
        self.b.board = [["." for _ in range(8)] for _ in range(8)]
        self.b.board[3][3] = "N"
        moves = self.b._knight_moves(3, 3, "white")

        self.assertEqual(len(moves), 8)

    def test_knight_in_the_corner(self):
        self.b.board = [["." for _ in range(8)] for _ in range(8)]
        self.b.board[0][0] = "N"
        moves = self.b._knight_moves(0, 0, "white")

        self.assertEqual(len(moves), 2)    

    