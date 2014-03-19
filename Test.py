import unittest
import Deck

class test(unittest.TestCase):

    def test_deck(self):
        tester = Deck.Deck()
        self.assertTrue(len(tester.deck) == 52)
        self.assertFalse(tester.isEmpty())
        self.assertEqual(tester.deck[51], tester.draw_card())

    def test_deck_b(self):
        tester = Deck.Deck_B()
        self.assertEqual(tester.deck_b, [])

    def test_table(self):
        tester = Deck.Table()
        self.assertTrue(len(tester.table) == 7)
        for col_idx, collumn in enumerate(tester.table):
            self.assertTrue(len(tester.table[col_idx]) == 5)
            for slot_idx, slot in enumerate(collumn):
                self.assertEquals(tester.table[col_idx][slot_idx], 0) 

    def test_game(self):
        tester = Deck.Game()
        self.assertTrue(len(tester.table.table) == 7)
        for col_idx, collumn in enumerate(tester.table.table):
            self.assertTrue(len(tester.table.table[col_idx]) == 5)
            for slot_idx, slot in enumerate(collumn):
                self.assertFalse(collumn[slot_idx] == 0)
                
        deck1 = tester.table.table
        tester.new_game()
        deck2 = tester.table.table

        self.assertTrue(deck1 != deck2)



if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
