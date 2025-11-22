import unittest
from shakki_ai.board import Board

class TestMakeUndo(unittest.TestCase):

    def test_make_undo_move(self):
        board = Board()
        move = board.parse_move("e2e4")

        board_snapshot = []
        for row in board.board:
            board_snapshot.append(row[:])

        turn_before = board.turn
        info = board.make_move(move)

        self.assertNotEqual(board.board, board_snapshot)

        board.undo_move(info)

        self.assertEqual(board.board, board_snapshot)
        self.assertEqual(board.turn, turn_before)



