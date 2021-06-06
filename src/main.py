"""
Evolution Simulator

A simple Predator-Prey Simulator
"""

__author__ = "Manas Mengle"
__version__ = "0.0.1"
__license__ = "GPLv3"


import random
import time
from enum import Enum, auto

creatures = []
new_creatures = []  # * Creatures to be added after current ones have gone to sleep
foods = []  # * Food 'map'. Each item holds int food amount


class State(Enum):
    SURVIVE = auto()
    REPRODUCE = auto()
    DIE = auto()


class Creature:
    def __init__(self):
        super(Creature, self).__init__()
        self.hunger = 0
        self.food_index = None  # * Index of food list
        self.alive = True

    def reset_hunger(self):
        self.hunger = 0

    def pick_food(self):
        self.food_index = random.randint(
            1, len(foods) - 1
        )  # len - 1 due to last index of list being len - 1, not len

    def eat_food(self):
        self.hunger = foods[self.food_index]

    def sleep(self):
        if self.hunger == 0:
            # Die
            self.alive = False
            return State.DIE
        elif self.hunger == 1:
            # Survive
            return State.SURVIVE
        elif self.hunger == 2:
            # Reproduce
            new_creatures.append(Creature())
            return State.REPRODUCE


def reset_creatures(amount=12):
    global creatures
    for i in range(amount):
        creatures.append(Creature())  # Creates 12 empty creatures


def reset_food(amount=60):
    global foods
    foods = [2] * amount  # Resets Food


def reset_hunger():
    for creature in creatures:
        if creature.alive:
            creature.reset_hunger()


def pick_all_food():
    for creature in creatures:
        if creature.alive:
            creature.pick_food()


def eat_all_food():
    # TODO: Add double detection
    for creature in creatures:
        if creature.alive:
            creature.eat_food()
            foods[creature.food_index] -= creature.hunger


def sleep_all():
    for creature in creatures:
        if creature.alive:
            state = creature.sleep()
            if state == State.SURVIVE:
                print("Creature", creatures.index(creature) + 1, "survived.")
            elif state == State.REPRODUCE:
                print("Creature", creatures.index(creature) + 1, "reproduced.")
            elif state == State.DIE:
                print("Creature", creatures.index(creature) + 1, "died.")

    creatures.extend(new_creatures)
    new_creatures.clear()


def print_food():
    print("\n\n")
    print("Food: ", end="")
    for food in foods:
        print(food, end="")
        time.sleep(0.1)


def print_creatures():
    print("\n\n")
    print("Number of creatures:", len(creatures))
    print("\nCreature | Hunger")
    for creature in creatures:
        if creature.alive:
            print(creatures.index(creature) + 1, creature.hunger)
            time.sleep(0.2)


def main_game_loop(days, creature_amount, food_amount):
    reset_creatures(creature_amount)
    for day in range(days):
        time.sleep(10)
        print("\n\n DAY", day + 1, "\n\n")
        reset_food(food_amount)
        print_food()
        time.sleep(2)
        print_creatures()
        time.sleep(5)
        pick_all_food()
        print("Food Picked")
        eat_all_food()
        time.sleep(4)
        print("Food Eaten")
        print_creatures()
        time.sleep(5)
        print_food()
        time.sleep(4)
        print("\nCreatures Reproduced, survived or died")
        sleep_all()
        time.sleep(4)
        reset_hunger()


def main():
    print("EVOLUTION SIMULATOR")
    print(
        "This game simulates the evolution of creature count and explores ideas of overpopulation, and equilibrium."
    )
    print(
        "The game starts off with a set amount of creatures, who are trying to find food."
    )
    print(
        "Each day, a set amount of food spawns at certain locations. The creatures can then pick a food location. The creatures then eat the food."
    )  # ? Add commandline args here
    print(
        "As the creatures go to sleep at the end of the day, depending on how much they have eaten, they can either die, survive, or reproduce."
    )
    print("The cycle then repeats for the following days.")
    time.sleep(10)
    # TODO: Add Command line args
    # ? first come, first serve or sharing switch
    main_game_loop(2, 12, 60)  # ? Reducing food amount?


if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()
