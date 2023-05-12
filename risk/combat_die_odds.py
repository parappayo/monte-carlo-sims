import random
import trials


def d6(count):
    result = [random.randrange(1, 6) for n in range(count)]
    result.sort(reverse=True)
    return result


def evalResult1v1(attackRoll, defendRoll):
    attackLoss, defendLoss = 0, 0

    if attackRoll[0] > defendRoll[0]:
        defendLoss += 1
    else:
        attackLoss += 1

    return (attackLoss, defendLoss)


def evalResult2v2(attackRoll, defendRoll):
    attackLoss, defendLoss = 0, 0

    if attackRoll[0] > defendRoll[0]:
        defendLoss += 1
    else:
        attackLoss += 1

    if attackRoll[1] > defendRoll[1]:
        defendLoss += 1
    else:
        attackLoss += 1

    return (attackLoss, defendLoss)


def roll3vs2():
    """Returns a tuple (attacker losses, defender losses)."""
    return evalResult2v2(d6(3), d6(2))


def roll2vs2():
    """Returns a tuple (attacker losses, defender losses)."""
    return evalResult2v2(d6(2), d6(2))


def roll3vs1():
    """Returns a tuple (attacker losses, defender losses)."""
    return evalResult1v1(d6(3), d6(1))


def roll2vs1():
    """Returns a tuple (attacker losses, defender losses)."""
    return evalResult1v1(d6(2), d6(1))


def roll1vs1():
    """Returns a tuple (attacker losses, defender losses)."""
    return evalResult1v1(d6(1), d6(1))


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

    printTrials('3 vs 2', roll3vs2, trialCount, keyCaptions)
    printTrials('2 vs 2', roll2vs2, trialCount, keyCaptions)
    printTrials('3 vs 1', roll3vs1, trialCount, keyCaptions)
    printTrials('2 vs 1', roll2vs1, trialCount, keyCaptions)
    printTrials('1 vs 1', roll1vs1, trialCount, keyCaptions)
