
import trials

def evalResult2v2(attackRoll, defendRoll):
    attackLoss, defendLoss = 0, 0

    attackRoll.sort(reverse=True)
    defendRoll.sort(reverse=True)

    if attackRoll[0] > defendRoll[0]:
        defendLoss += 1
    else:
        attackLoss += 1

    if attackRoll[1] > defendRoll[1]:
        defendLoss += 1
    else:
        attackLoss += 1

    return (attackLoss, defendLoss)


def everyDoubleRoll():
    for die1 in range(1, 7):
        for die2 in range(1, 7):
            yield [die1, die2]


def everyTripleRoll():
    for die1 in range(1, 7):
        for die2 in range(1, 7):
            for die3 in range(1, 7):
                yield [die1, die2, die3]


def everyCombatRoll():
    for attackRoll in everyTripleRoll():
        for defendRoll in everyDoubleRoll():
            yield (attackRoll, defendRoll)


def compileResults():
    results = {}
    count = 0
    for attackRoll, defendRoll in everyCombatRoll():
        result = evalResult2v2(attackRoll, defendRoll)
        if not result in results:
            results[result] = 1
        else:
            results[result] += 1
        count += 1
    return (results, count)


if __name__ == '__main__':
    (results, count) = compileResults()
    print("expected iterations: ", pow(6, 5))
    print("ran iterations: ", count)
    print(results)

    keyCaptions = {
        (0, 2): 'defender loses 2',
        (1, 1): 'each lose 1',
        (2, 0): 'attacker loses 2',
        (0, 1): 'defender loses 1',
        (1, 0): 'attacker loses 1'
    }

    trials.normalizeCounts(results, count)
    print(trials.formatToCSV(results, keyCaptions))
