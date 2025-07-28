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

	def test_land_count(self):
		deck = mtg.Deck()
		deck.generate(60, 24)
		lands = [card for card in deck.cards if card.type == "land"]
		self.assertEqual(len(lands), 24)

		deck.shuffle()
		lands = [card for card in deck.cards if card.type == "land"]
		self.assertEqual(len(lands), 24)


if __name__ == "__main__":
	unittest.main()
