import mtg
import trials


def evalDraw(deck: mtg.Deck, drawCount):
	deck.shuffle()
	return mtg.count_cards_of_type(deck.peek_top(drawCount), "land")


def evalDrawTwoColour(deck: mtg.Deck, drawCount):
	deck.shuffle()
	hand = deck.peek_top(drawCount)
	return (mtg.count_cards_of_type(hand, "mountain"), mtg.count_cards_of_type(hand, "forest"))


def printTrials(caption, trialFunc, trialCount):
	print(caption)
	results = trials.run(trialFunc, trialCount)
	trials.normalizeCounts(results, trialCount)
	print(trials.formatToCSV(results))


def singleColourTrial(deckSize, landCount, drawCount):
	deck = mtg.Deck()
	deck.add_cards(deckSize - landCount, "creature")
	deck.add_cards(landCount, "land")
	printTrials(
		f'deck size {deckSize}, land count {landCount}, draw {drawCount}',
		lambda: evalDraw(deck, drawCount),
		trialCount)


def twoColourTrial(deckSize, mountainCount, forestCount, drawCount):
	deck = mtg.Deck()
	deck.add_cards(deckSize - mountainCount - forestCount, "creature")
	deck.add_cards(mountainCount, "mountain")
	deck.add_cards(forestCount, "forest")
	printTrials(
		f'deck size {deckSize}, moutain count {mountainCount}, forestCount {forestCount}, draw {drawCount}',
		lambda: evalDrawTwoColour(deck, drawCount),
		trialCount)


def singleColourTrials(trialCount):
	singleColourTrial(60, 24, 7)
	singleColourTrial(60, 23, 7)
	singleColourTrial(60, 22, 7)
	singleColourTrial(60, 21, 7)

	singleColourTrial(40, 18, 7)
	singleColourTrial(40, 17, 7)
	singleColourTrial(40, 16, 7)


def twoColourTrials(trialCount):
	twoColourTrial(60, 12, 12, 7)
	twoColourTrial(60, 11, 13, 7)
	twoColourTrial(60, 10, 14, 7)
	twoColourTrial(60, 9, 15, 7)
	twoColourTrial(60, 8, 16, 7)

	twoColourTrial(60, 12, 11, 7)
	twoColourTrial(60, 11, 11, 7)
	twoColourTrial(60, 10, 11, 7)
	twoColourTrial(60, 9, 11, 7)
	twoColourTrial(60, 8, 11, 7)

	twoColourTrial(60, 12, 10, 7)
	twoColourTrial(60, 11, 10, 7)
	twoColourTrial(60, 10, 10, 7)
	twoColourTrial(60, 9, 10, 7)
	twoColourTrial(60, 8, 10, 7)

	singleColourTrial(40, 9, 9, 7)
	singleColourTrial(40, 8, 10, 7)
	singleColourTrial(40, 7, 11, 7)
	singleColourTrial(40, 6, 12, 7)

	singleColourTrial(40, 9, 8, 7)
	singleColourTrial(40, 8, 9, 7)
	singleColourTrial(40, 7, 10, 7)
	singleColourTrial(40, 6, 11, 7)


if __name__ == "__main__":
	trialCount = 200_000

	singleColourTrials(trialCount)
	twoColourTrials(trialCount)
