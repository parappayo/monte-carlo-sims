from dice import d6


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


def evalResult1v1(attackRoll, defendRoll):
    attackLoss, defendLoss = 0, 0

    if attackRoll[0] > defendRoll[0]:
        defendLoss += 1
    else:
        attackLoss += 1

    return (attackLoss, defendLoss)


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
