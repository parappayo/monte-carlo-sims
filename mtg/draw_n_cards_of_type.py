import mtg
import trials


def evalDraw(deck: mtg.Deck, drawCount):
	deck.shuffle()
	drawnCards = deck.cards[0:drawCount]
	return mtg.count_cards_of_type(drawnCards, "land")


def printTrials(caption, trialFunc, trialCount):
	print(caption)
	results = trials.run(trialFunc, trialCount)
	trials.normalizeCounts(results, trialCount)
	print(trials.formatToCSV(results))


if __name__ == "__main__":
	trialCount = 200_000

	deck = mtg.Deck()
	deck.add_cards(36, "creature")
	deck.add_cards(24, "land")

	printTrials('deck size 60, land count 24, draw 7', lambda: evalDraw(deck, 7), trialCount)
	printTrials('deck size 60, land count 23, draw 7', lambda: evalDraw(deck, 7), trialCount)
	printTrials('deck size 60, land count 22, draw 7', lambda: evalDraw(deck, 7), trialCount)
	printTrials('deck size 60, land count 21, draw 7', lambda: evalDraw(deck, 7), trialCount)
	printTrials('deck size 40, land count 18, draw 7', lambda: evalDraw(deck, 7), trialCount)
	printTrials('deck size 40, land count 17, draw 7', lambda: evalDraw(deck, 7), trialCount)
	printTrials('deck size 40, land count 16, draw 7', lambda: evalDraw(deck, 7), trialCount)
