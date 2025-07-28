import mtg
import trials


def evalDraw(deck: mtg.Deck, drawCount):
	deck.shuffle()
	drawnCards = deck.cards[0:drawCount]
	return mtg.land_count(drawnCards)


def printTrials(caption, trialFunc, trialCount):
	print(caption)
	results = trials.run(trialFunc, trialCount)
	trials.normalizeCounts(results, trialCount)
	print(trials.formatToCSV(results))


if __name__ == "__main__":
	trialCount = 200_000

	deck = mtg.Deck()
	deck.generate(60, 24)

	printTrials('draw 7', lambda: evalDraw(deck, 7), trialCount)
