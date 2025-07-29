import random


class Card:
	def __init__(self, type):
		self.type = type


class Deck:
	def __init__(self):
		self.cards = []

	def __len__(self):
		return len(self.cards)

	def shuffle(self):
		random.shuffle(self.cards)

	def add_cards(self, count, type):
		self.cards.extend([Card(type) for i in range(0, count)])

	def cards_of_type(self, cardType):
		return [card for card in self.cards if card.type == cardType]


def count_cards_of_type(cards, type):
	return len([card for card in cards if card.type == type])
