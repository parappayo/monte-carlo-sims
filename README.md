# monte-carlo-sims

Small programs to simulate probabilistic situations

The goal is to learn stuff and to shake the cobwebs out of my head. This repo contians small [Monte Carlo sampling](https://en.wikipedia.org/wiki/Monte_Carlo_method) simulations that can be helpful to validate problem solution proofs using [combinatorics](https://en.wikipedia.org/wiki/Combinatorics). It may also serve as a helpful reference for fun stats problems to draw on.

## Simulations

* `/mtg` contains simulations relating to [Magic: The Gathering](https://en.wikipedia.org/wiki/Magic:_The_Gathering), a card game that is ripe for different probability distribution scenarios.
* `/risk` contains simulations relating to [Risk](https://en.wikipedia.org/wiki/Risk_(game)), a turn-based strategy game with some simple dice rolling scenarios.

## TODO

* trials.py module should go in a common helper package
* some kind of root level Makefile or other such build script might help

## Project Ideas

Some ideas of stuff I want to sim,

* Traditional card games like [Hearts](https://en.wikipedia.org/wiki/Hearts_(card_game)) and [Texas Hold'em](https://en.wikipedia.org/wiki/Texas_hold_%27em) are well known for probability scenarios.
* [Dungeons & Dragons](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons) is known for elaborate dice rolling scenarios, mostly because it does not limit itself to six sided dice.
* [Trombone Champ](https://en.wikipedia.org/wiki/Trombone_Champ) hot dog cards are a variation on the MtG stuff.
  * A player task is to collect 10x copies of a [Hot Dog card](https://trombone-champ.fandom.com/wiki/Hot_Dog). What the probablility distribution is for how many packs the user needs to open, and what is the probability of having such-and-such more duplicates of some other card than Hot Dog?
* [Ogre](https://en.wikipedia.org/wiki/Ogre_(board_game)) is another turn-based strategy game, with a Combat Results Table (CRT).
  * What is the optimal allocation of firepower when targetting units of varying defensive strengths? Is the Ogre player better off making many small, riskier bets or fewer less risky bets?
