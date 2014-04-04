import unittest, pygame
import Deck, Golf_relaxed, Card, readData

class test(unittest.TestCase):
    pygame.init()
    screen = pygame.display.set_mode((800, 500))

    def test_deck(self):
        tester = Deck.Deck()
        self.assertTrue(len(tester.deck) == 53)
        self.assertFalse(tester.isEmpty())
        self.assertEqual(tester.deck[52], tester.get())

    def test_Golf_relaxed(self):
        tester = Golf_relaxed.Golf_relaxed()
        colList = [tester.col1, tester.col2, tester.col3, tester.col4, tester.col5, tester.col6, tester.col7]
        for idx, col in enumerate(colList):
            self.assertTrue(len(col) == 5)
        self.assertTrue(len(tester.deckA) == 17)
        self.assertEqual(len(tester.deckB), 1)

    def test_Card(self):
        tester = Card.Card('H1')
        self.assertTrue(tester.rank == '1')
        self.assertFalse(tester.selected == True)       

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
