# Monte Carlo Sims - Magic: The Gathering

[Magic: The Gathering](https://en.wikipedia.org/wiki/Magic:_The_Gathering) is a popular card game invented by [Richard Garfield](https://en.wikipedia.org/wiki/Richard_Garfield).

## TODO

* Tweak the CSV output to be more useful as a data set
* How many booster packs to collect a set given varying rarity conditions?
* Odds of drawing a specific hand, eg. three different combo pieces needing to be present in N cards with 4 copies each

## Simulations

### Draw N Lands

One of the simplest MtG scenarios is calculating the odds of drawing N "land cards" with M draws. In a typical game setup, a player's deck is 60 cards, there are 24 land cards within the deck, and the player draws 7 cards for their opening hand. A result of 2 or 3 lands drawn is desirable. Of course the same simulation can be adapted to figure how many creature cards would be drawn, how many cards of a certain mana cost, etc.

See also: [Binomial Coefficient](https://en.wikipedia.org/wiki/Binomial_coefficient)

Example output:

```
deck size 60, land count 24, draw 7
0,1,2,3,4,5,6,7
0.021705,0.119875,0.26993,0.308905,0.196355,0.07012,0.012135,0.000975
deck size 60, land count 23, draw 7
0,1,2,3,4,5,6,7
0.021365,0.1217,0.26797,0.308955,0.198105,0.069015,0.011895,0.000995
deck size 60, land count 22, draw 7
0,1,2,3,4,5,6,7
0.0222,0.11995,0.26922,0.309855,0.19599,0.06945,0.012375,0.00096
deck size 60, land count 21, draw 7
0,1,2,3,4,5,6,7
0.02061,0.120885,0.27065,0.308885,0.1964,0.069385,0.012255,0.00093
deck size 40, land count 18, draw 7
0,1,2,3,4,5,6,7
0.022205,0.121075,0.269405,0.30806,0.196895,0.06927,0.012165,0.000925
deck size 40, land count 17, draw 7
0,1,2,3,4,5,6,7
0.02182,0.12064,0.27108,0.30862,0.196775,0.06797,0.012325,0.00077
deck size 40, land count 16, draw 7
0,1,2,3,4,5,6,7
0.02159,0.12111,0.26731,0.309205,0.19807,0.069305,0.01235,0.00106
```
