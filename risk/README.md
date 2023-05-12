# Monte Carlo Sims - Risk

[Risk](https://en.wikipedia.org/wiki/Risk_(game)) is a turn-based conquest game that involves comparing rolls on six-sided dice.

## Simulations

### Combat Die Odds

See `combat_die_odds.py` for simulation code.

The obvious question players have regarding die roll probabilities when playing Risk is how advantageous it is for an attacker to employ 3 dice when attacking rather than 2 or 1. There is the temptation to think that because fewer armies are staked when attacking with fewer dice, that it works out in the attacker's favour. Similarly, a defending player has the option to only stake 1 army instead of 2.

There are further variations where one or both sides has a general (grants +1 to the highest die roll for that side), or the defender has a fortification bonus (I need to look up the rules on that.)

This question is pretty trivial to solve by categorizing each die roll combination by the outcome that it produces. The outcomes are one of the following:

* Attacker loses 2
* Attacker loses 1, defender loses 1
* Defender loses 2
* Attacker loses 1
* Defender loses 1

Having worked out the precise probabilities of each situation, combat round eval can be reduced to a single RNG roll and a table lookup rather than generating separate rolls for each of the dice involved. While this optimization may upset players, it is much faster for simulation purposes.

Sample output:

```
$ python combat_die_odds.py
3 vs 2
defender loses 2,each lose 1,attacker loses 2
0.346505,0.341675,0.31182
2 vs 2
defender loses 2,each lose 1,attacker loses 2
0.20777,0.32055,0.47168
3 vs 1
defender loses 1,attacker loses 1
0.64112,0.35888
2 vs 1
defender loses 1,attacker loses 1
0.5605,0.4395
1 vs 1
defender loses 1,attacker loses 1
0.40065,0.59935
```

### Cost of Capturing a Territory

See `cost_to_capture.py` for simulation code.

Given that the problem of how to efficiently deploy combat dice is solved (per the previous section), it is easier now to answer the question of what the distribution is for how many armies an attacker must spend in order to capture a territory given how many armies are defending it.

Generating a look-up table for cost-to-capture is particularly helpful for AI search approaches, since Risk is a game where the cost to get from one board position to another needs to be taken into account.

Sample output:

```
$ python cost_to_capture.py 10
0,5,10,15,20,25,30,35
0.1944,0.4395,0.2656,0.0799,0.0172,0.003,0.0002,0.0002

$ python cost_to_capture.py 50
10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85
0.0004,0.0029,0.0162,0.0571,0.1175,0.1772,0.1961,0.173,0.1198,0.0738,0.0391,0.0161,0.0071,0.002,0.0016,0.
0001

$ python cost_to_capture.py 500
325,330,335,340,345,350,355,360,365,370,375,380,385,390,395,400,405,410,415,420,425,430,435,440,445,450,4
55,460,465,470,475,480,485,490,495,500,505,510,515,520,525,530,535,540,545,550
0.0003,0.0005,0.0005,0.0012,0.0009,0.003,0.0033,0.0046,0.0078,0.01,0.0122,0.0177,0.0219,0.0262,0.0314,0.0
4,0.0413,0.048,0.0526,0.0547,0.0581,0.0608,0.0619,0.0584,0.061,0.0504,0.0478,0.042,0.0346,0.0339,0.0245,0
.0232,0.0143,0.0127,0.0102,0.0097,0.0074,0.004,0.0024,0.001,0.001,0.001,0.0009,0.0004,0.0001,0.0002
```

### Probability to Capture a Territory

Finding out the odds of an attacker succeeding or failing to capture a given territory is solveable as a subset of cost-to-capture, since the number of armies available to the attacker can be taken as a cut-line. Sum up the total distribution that is less than the number of armies availble to the attacker, and that is the probability of success.
