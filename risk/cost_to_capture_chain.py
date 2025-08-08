import dice
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


def evalCaptureChain(attackerCount, chain, i = 0):
    """Returns a tuple (territoryCapturedCount, attackerArmiesRemainingCount)"""
    if i < len(chain):
        cost = costToCapture(chain[i]) + 1  # note +1 here because attacker has to leave an army behind
        if attackerCount > cost:
            return evalCaptureChain(attackerCount - cost, chain, i + 1)
        return (i, 0)
    return (i, attackerCount)


if __name__ == '__main__':
    trialCount = 200_000
    attackerCount = 30
    territoryChain = [12, 3, 1, 1, 1, 1]
    (territoryCapturedCount, attackerArmiesRemainingCount) = evalCaptureChain(attackerCount, territoryChain)

    print(
        "trials", trialCount,
        "attackers", attackerCount,
        "defenders", territoryChain)

    results = trials.run(lambda: evalCaptureChain(attackerCount, territoryChain), trialCount)
    trials.normalizeCounts(results, trialCount)
    print(trials.formatToCSV(results))
