import dice


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
        cost = costToCapture(chain[i])
        if attackerCount > cost:
            return evalCaptureChain(attackerCount - cost, chain, i + 1)
        return (i, 0)
    return (i, attackerCount)


if __name__ == '__main__':
    attackerCount = 30
    territoryChain = [5, 3, 5, 7, 1, 1]
    (territoryCapturedCount, attackerArmiesRemainingCount) = evalCaptureChain(attackerCount, territoryChain)
    print(
        "Input: attackers", attackerCount,
        "defenders", territoryChain)
    print(
        "Result: captured territory count", territoryCapturedCount,
        "attacker armies remaining", attackerArmiesRemainingCount)
