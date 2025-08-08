import risk
import trials


def printTrials(caption, trialFunc, trialCount, keyCaptions):
    print(caption)
    results = trials.run(trialFunc, trialCount)
    trials.normalizeCounts(results, trialCount)
    print(trials.formatToCSV(results, keyCaptions))


if __name__ == '__main__':
    trialCount = 200_000

    keyCaptions = {
        (0, 2): 'defender loses 2',
        (1, 1): 'each lose 1',
        (2, 0): 'attacker loses 2',
        (0, 1): 'defender loses 1',
        (1, 0): 'attacker loses 1'
    }

    printTrials('3 vs 2', risk.roll3vs2, trialCount, keyCaptions)
    printTrials('2 vs 2', risk.roll2vs2, trialCount, keyCaptions)
    printTrials('3 vs 1', risk.roll3vs1, trialCount, keyCaptions)
    printTrials('2 vs 1', risk.roll2vs1, trialCount, keyCaptions)
    printTrials('1 vs 1', risk.roll1vs1, trialCount, keyCaptions)
