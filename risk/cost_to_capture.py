import random
import sys
import trials


def d6(count):
    result = [random.randrange(1, 6) for n in range(count)]
    result.sort(reverse=True)
    return result


def roll3v2():
    """Generate a random combat result, returns a tuple (attacker losses, defender losses)."""
    roll = random.random()
    if roll < 0.37165637860082307:
        return (0, 2)
    if roll < 0.37165637860082307 + 0.3357767489711934:
        return (2, 0)
    return (1, 1)


def roll3v1():
    attackers, defenders = d6(3), d6(1)
    if attackers[0] > defenders[0]:
        return (0, 1)
    return (1, 0)


def costToConquer(defenderCount):
    cost = 0
    while defenderCount > 1:
        result = roll3v2()
        cost += result[0]
        defenderCount -= result[1]
    while defenderCount > 0:
        result = roll3v1()
        cost += result[0]
        defenderCount -= result[1]
    return cost


if __name__ == '__main__':
    trialCount = 100_000
    defenderCount = int(sys.argv[1])
    bucketSize = 5

    results = trials.run(lambda: costToConquer(defenderCount), trialCount, bucketSize)
    trials.normalizeCounts(results, trialCount)
    print(trials.formatToCSV(results))
