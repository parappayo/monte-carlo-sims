import random


class Card:
	def __init__(self, type):
		self.type = type


class Deck:
	def __init__(self):
		self.cards = []

	def generate(self, size, landCardCount):
		creatureCardCount = size - landCardCount
		self.cards = [Card("creature") for i in range(1, creatureCardCount)]
		self.cards.extend([Card("land") for i in range(1, landCardCount)])

	def shuffle(self):
		random.shuffle(self.cards)
