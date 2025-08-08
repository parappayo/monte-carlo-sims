import risk
import trials


def compileResults():
    results = {}
    count = 0
    for attackRoll, defendRoll in risk.everyCombatRoll():
        result = risk.evalResult2v2(attackRoll, defendRoll)
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
