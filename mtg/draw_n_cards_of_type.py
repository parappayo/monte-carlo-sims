import mtg
import trials


def evalDraw(deck: mtg.Deck, drawCount):
	for card in deck.cards[0:drawCount]:
		print(card.type)


if __name__ == "__main__":
	deck = mtg.Deck()
	deck.generate(60, 24)
	deck.shuffle()
	evalDraw(deck, 7)
