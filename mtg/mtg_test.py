import mtg
import unittest


class TestDeck(unittest.TestCase):

	def test_len(self):
		deck = mtg.Deck()
		self.assertEqual(len(deck), 0)
		self.assertEqual(len(deck.cards), 0)

		deck.add_cards(36, "creature")
		self.assertEqual(len(deck), 36)
		self.assertEqual(len(deck.cards), 36)

		deck.add_cards(24, "land")
		self.assertEqual(len(deck), 60)
		self.assertEqual(len(deck.cards), 60)

	def test_cards_of_type(self):
		deck = mtg.Deck()
		deck.add_cards(36, "creature")
		deck.add_cards(24, "land")

		lands = deck.cards_of_type("land")
		self.assertEqual(len(lands), 24)

		deck.shuffle()
		lands = deck.cards_of_type("land")
		self.assertEqual(len(lands), 24)

	def test_peek_top(self):
		deck = mtg.Deck()
		deck.add_cards(60, "card")
		topCards = deck.peek_top(7)
		self.assertEqual(len(topCards), 7)


if __name__ == "__main__":
	unittest.main()
