import dice
import sys
import trials


def costToCapture(defenderCount):
    cost = 0
    while defenderCount > 1:
        result = dice.roll3v2()
        cost += result[0]
        defenderCount -= result[1]
    while defenderCount > 0:
        result = dice.roll3v1()
        cost += result[0]
        defenderCount -= result[1]
    return cost


if __name__ == '__main__':
    trialCount = 100_000
    defenderCount = int(sys.argv[1])
    bucketSize = 5

    results = trials.run(lambda: costToCapture(defenderCount), trialCount, bucketSize)
    trials.normalizeCounts(results, trialCount)
    print(trials.formatToCSV(results))
