import unittest
import Kapall

class test(unittest.TestCase):

    def test_deck(self):
        tester = Kapall.Deck()
        self.assertTrue(len(tester.deck) == 52)
        self.assertFalse(tester.isEmpty())
        self.assertEqual(tester.deck[51], tester.draw_card())

    def test_deck_b(self):
        tester = Kapall.Deck_B()
        self.assertEqual(tester.deck_b, [])

    def test_board(self):
        tester = Kapall.Board()
        self.assertTrue(len(tester.board) == 7)
        for col_idx, collumn in enumerate(tester.board):
            self.assertTrue(len(tester.board[col_idx]) == 5)
            for slot_idx, slot in enumerate(collumn):
                self.assertEquals(tester.board[col_idx][slot_idx], 0) 

    def test_game(self):
        tester = Kapall.Game()
        self.assertTrue(len(tester.board.board) == 7)
        for col_idx, collumn in enumerate(tester.board.board):
            self.assertTrue(len(tester.board.board[col_idx]) == 5)
            for slot_idx, slot in enumerate(collumn):
                self.assertFalse(collumn[slot_idx] == 0)

        deck1 = tester.board.board
        tester.new_game()
        deck2 = tester.board.board

        self.assertTrue(deck1 != deck2)


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
