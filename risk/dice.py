import random


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
