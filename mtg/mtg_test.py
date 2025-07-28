import mtg
import unittest


class TestDeck(unittest.TestCase):

	def test_len(self):
		deck = mtg.Deck()
		self.assertEqual(len(deck), 0)
		self.assertEqual(len(deck.cards), 0)
		deck.generate(60, 24)
		self.assertEqual(len(deck), 60)
		self.assertEqual(len(deck.cards), 60)


if __name__ == "__main__":
	unittest.main()
