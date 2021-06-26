"""
Evolution Simulator

A simple Predator-Prey Simulator
"""

__author__ = "Manas Mengle"
__version__ = "0.3.3-dev0"
__license__ = "GPLv3"

import simulator
import time
import argparse


def main(args):
    """Main entry point of the app"""
    if not args.noverbosity:
        print("EVOLUTION SIMULATOR")
        print(
            "This game simulates the evolution of creature count and explores ideas of overpopulation, and equilibrium."
        )
        print(
            "The game starts off with a set amount of creatures, who are trying to find food."
        )
        print(
            "Each day, a set amount of food spawns at certain locations. The creatures can then pick a food location. The creatures then eat the food."
        )
        print(
            "As the creatures go to sleep at the end of the day, depending on how much they have eaten, they can either die, survive, or reproduce."
        )
        print("The cycle then repeats for the following days.")
        None if args.pause > 1 else time.sleep(10)

        print("\n\n", "Running Simulation with:")
        print(args.days, "days.")
        print(args.start_creatures, "starting creatures.")
        print(args.food_amount, "available food locations.")
    simulator.main_game_loop(
        int(args.days),
        int(args.start_creatures),
        int(args.food_amount),
        args.noverbosity,
        args.savejson,
        args.pause,
    )  # ? Reducing food amount?


if __name__ == "__main__":
    """This is executed when run from the command line"""
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("days", help="number of days to simulate")

    # Required positional argument
    parser.add_argument("start_creatures", help="number of starting creatures")

    # Required positional argument
    parser.add_argument("food_amount", help="number of food positions")

    # Optional argument flag which defaults to False
    parser.add_argument(
        "-s",
        "--share",
        action="store_true",
        default=False,
        help="whether the creatures should share the food evenly if two of them end up at the same food position, CURRENTLY NOT WORKING",
    )

    # Optional argument flag which defaults to True
    parser.add_argument(
        "-sj",
        "--savejson",
        action="store_false",
        default=True,
        help="Simulator automatically saves simulation data to JSON file. Use flag to stop this.",
    )

    # Optional argument flag which defaults to False
    parser.add_argument(
        "-nv",
        "--noverbosity",
        action="store_true",
        default=False,
        help="Run Simulation instantly, without interactivity, and output a graph of the results.",
    )

    # Optional pause counter (eg. -p, -pp, -ppp, etc.)
    parser.add_argument(
        "-p",
        "--pause",
        action="count",
        default=0,
        help="pause (-p = no pauses, except between days, -pp = no pauses, etc)",
    )

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__),
    )

    args = parser.parse_args()
    main(args)
