# Nim-AI

![Version](https://img.shields.io/badge/version-1.0.0--beta-blue.svg?cacheSeconds=2592000)

> Play a game of nim against an AI trained with Q-learning.

[Nim](https://en.wikipedia.org/wiki/Nim) is a game wherein two players take turns picking objects from piles with the goal to force the other player to pick the last object. On their turn, a player can pick one or several from a single pile. The players take turns picking objects from the piles until there are none remaining. The last player who picked loses.

[Q-learning](https://en.wikipedia.org/wiki/Q-learning) is a variety of reinforcement learning where an agent learns the value of an action in a particular state. This is acheived by a reward system which can be modified by variables α and ε, which impact how quickly the agent makes changes to its knowledge base and how random these changes are, respectively.

## Install

```sh
$ wget https://github.com/ConnerRose/nim-ai/releases/download/v1.0-beta/nim_ai.exe
```

Or download `nim_ai.exe` from https://github.com/ConnerRose/nim-ai/releases/tag/v1.0-beta.

## Usage

```sh
$ ./nim_ai.exe
```

| Option                                            | Description                          | Type    | Default        | Required? |
| ------------------------------------------------- | ------------------------------------ | ------- | -------------- | --------- |
| `-h --help`                                       | Show these options                   | `None`  | `None`         | No        |
| `-n NUM_GAMES, --num-games NUM_GAMES`             | Number of training games             | `int`   | `1000`         | No        |
| `-a ALPHA, --alpha ALPHA`                         | Alpha (learning rate), (0 <= α <= 1) | `float` | `0.5`          | No        |
| `-e EPSILON, --epsilon EPSILON`                   | Epsilon (randomness), (0 <= ε <= 1)  | `float` | `0.1`          | No        |
| `-p PILES [PILES ...], --piles PILES [PILES ...]` | Specify piles in game                | `int`   | `[1, 3, 5, 7]` | No        |

## Author

**Conner Rose**

- Github: [@ConnerRose](https://github.com/ConnerRose)
- LinkedIn: [@ConnerRose](https://linkedin.com/in/ConnerRose)
