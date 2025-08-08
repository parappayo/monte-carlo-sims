# Monte Carlo Sims - Risk

[Risk](https://en.wikipedia.org/wiki/Risk_(game)) is a turn-based conquest game that involves comparing rolls on six-sided dice.

## TODO

* Simulations having to do with leaders and fortresses

## Simulations

### Combat Die Odds

See `combat_die_odds_monte_carlo.py` for simulation code.

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
$ python combat_die_odds_brute_force.py
expected iterations:  7776
ran iterations:  7776
{(2, 0): 2275, (1, 1): 2611, (0, 2): 2890}
defender loses 2,each lose 1,attacker loses 2
0.37165637860082307,0.3357767489711934,0.2925668724279835
```

```
$ python combat_die_odds_monte_carlo.py
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
0,5,10,15,20,25,30,35,40
0.17825,0.41182,0.2771,0.09869,0.0275,0.00546,0.00106,0.00011,1e-05

$ python cost_to_capture.py 50
5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,115
2e-05,0.00017,0.00229,0.01244,0.04112,0.08834,0.14084,0.17648,0.17114,0.14524,0.09857,0.06302,0.0333,0.0160
9,0.00648,0.00296,0.00103,0.00032,8e-05,3e-05,3e-05,1e-05

$ python cost_to_capture.py 500
310,330,335,340,345,350,355,360,365,370,375,380,385,390,395,400,405,410,415,420,425,430,435,440,445,450,455
,460,465,470,475,480,485,490,495,500,505,510,515,520,525,530,535,540,545,550,555,560,565,570,575,580,585,59
0,595,600,605,610,615,620,625
1e-05,3e-05,2e-05,4e-05,6e-05,0.00022,0.00035,0.00057,0.00093,0.00168,0.00214,0.00326,0.00463,0.00656,0.009
07,0.01214,0.01472,0.0191,0.02251,0.02863,0.03228,0.03813,0.04161,0.04655,0.05027,0.05309,0.05694,0.05586,0
.05512,0.05483,0.05119,0.04879,0.04417,0.04132,0.03513,0.03237,0.02699,0.02357,0.01848,0.0158,0.01241,0.009
75,0.00719,0.0058,0.00429,0.00338,0.00246,0.00185,0.00119,0.00091,0.00056,0.00039,0.00024,0.00017,0.00014,1
e-05,6e-05,1e-05,1e-05,1e-05,1e-05
```

### Probability to Capture a Territory

Finding out the odds of an attacker succeeding or failing to capture a given territory is solveable as a subset of cost-to-capture, since the number of armies available to the attacker can be taken as a cut-line. Sum up the total distribution that is less than the number of armies availble to the attacker, and that is the probability of success.

### Probability to Capture a Chain of Territories

A common scenario in Risk-like games is that a player would like to capture a set of connected territories in some order. This adds a [Markov Chain](https://en.wikipedia.org/wiki/Markov_chain) element to the problem. The setup here is that given an ordered list of territories with defending army counts for each, and given a starting count of attacking armies, how far down the list can the attacker get, and how many attacking armies are left over, if any?

An important rule to account for is that the attacker must leave one army behind at each territory in the chain. In actual play the attacker may elect to leave behind as many armies as they choose, but for the purposes of deciding what the probable cost of conquering a chain of territories is, we can assume that the minimum mandatory one army is used.

This sim makes a simplifying assumption (for now) that the attacker always has 3 armies to attack with. In reality, once the attacker is down to their last 2 armies, they attack with reduced strength, and an attacker with only 1 army cannot attack. This may get ironed out in a future version.

Example output:

```
$ python cost_to_capture_chain.py
trials 200000 attackers 30 defenders [12, 3, 1, 1, 1, 1]
(0, 0),(1, 0),(2, 0),(3, 0),(4, 0),(5, 0),(6, 1),(6, 2),(6, 3),(6, 4),(6, 5),(6,
 6),(6, 7),(6, 8),(6, 9),(6, 10),(6, 11),(6, 12),(6, 13),(6, 14),(6, 15),(6, 16)
,(6, 17),(6, 18),(6, 19),(6, 20),(6, 21),(6, 22),(6, 23),(6, 24)
0.005065,0.016025,0.011995,0.017535,0.025575,0.03409,0.027235,0.032465,0.03744,0
.04243,0.047555,0.053785,0.058255,0.062195,0.0646,0.066765,0.064865,0.062265,0.0
5949,0.05208,0.045285,0.036855,0.028185,0.02025,0.013235,0.008215,0.00394,0.0016
7,0.000555,0.0001
```
