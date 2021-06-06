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
new_creatures = [] # * Creatures to be added after current ones have gone to sleep
foods = []  # * length of 60, int food in each

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
        self.food_index = random.randint(1, len(foods)-1) # len - 1 due to last index of list being len - 1, not len

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


def reset_creatures():
    global creatures
    for i in range(12):
        creatures.append(Creature())  # Creates 12 empty creatures
        


def reset_food():
    global foods
    foods = [2] * 60  # Resets Food

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
                print("Creature",creatures.index(creature)+1,"survived.")            
            elif state == State.REPRODUCE:
                print("Creature",creatures.index(creature)+1,"reproduced.")
            elif state == State.DIE:
                print("Creature",creatures.index(creature)+1,"died.")


    creatures.extend(new_creatures)
    new_creatures.clear()



def print_food():
    print('\n\n')
    print('Food: ', end='')
    for food in foods:
        print(food, end='')
def print_creatures():
    print('\n\n')
    print("Number of creatures:",len(creatures))
    print("\nCreature | Hunger")
    for creature in creatures:
        if creature.alive:
            print(creatures.index(creature)+1,creature.hunger)
def main_game_loop(days):
    reset_creatures()
    for day in range(days):
        time.sleep(10)
        print("\n\n DAY",day+1,"\n\n")
        reset_food()
        print_food()
        time.sleep(2)
        print_creatures()
        time.sleep(4)
        pick_all_food()
        print("Food Picked")
        eat_all_food()
        time.sleep(4)
        print("Food Eaten")
        print_creatures()
        time.sleep(4)
        print_food()
        time.sleep(4)
        print("\nCreatures Reproduced, survived or died")
        sleep_all()
        time.sleep(4)
        reset_hunger()
        print_creatures()

def main():
    print("hello world")
    main_game_loop(2)


if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()
