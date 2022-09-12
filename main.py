import argparse

from Util import play, train

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Play nim against an AI.')
    parser.add_argument(
        "-n", "--num-games", type=int, default=1000, help="Number of training games. Default=1000")
    parser.add_argument(
        "-a", "--alpha", type=float, default=0.5, help="Alpha (learning rate), (0 <= α <= 1). Default=0.5")
    parser.add_argument(
        "-e", "--epsilon", type=float, default=0.1, help="Epsilon (randomness), (0 <= ε <= 1). Default=0.1")
    parser.add_argument(
        "-p", "--piles", nargs='+', type=int, default=[1, 3, 5, 7], help="Specify piles. Default = [1 3 5 7]")
    args = parser.parse_args()

    ai = train(args.num_games, args.alpha, args.epsilon, args.piles)
    play(ai, piles=args.piles)
