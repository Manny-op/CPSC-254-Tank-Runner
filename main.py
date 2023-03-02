#! /usr/bin/env python3


"""The Tank Runner executable."""

from tankrunner.game import TankRunner


def main():
    """This function will runn the Tank Runner game."""
    game = TankRunner()
    return game.run()


if __name__ == '__main__':
    main()
