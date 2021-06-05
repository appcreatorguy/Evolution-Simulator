"""
Evolution Simulator

A simple Predator-Prey Simulator
"""

import random

__author__ = "Manas Mengle"
__version__ = "0.0.1"
__license__ = "GPLv3"

creatures = [] * 12
food = [] * 60 #* length of 60, int food in each
class Creature():
    def __init__(self):
        super(Creature, self).__init__()
        self.hunger = 0
        self.food_position = None #* Index of food list
        self.alive = True
    def pick_food(self, food_list = food):
        self.food_position = random.randint(1, len(food_list))
    def eat_food(self, food_list = food):
        self.hunger = food_list[self.food_position]
        food_list[self.food_position] = 0
    def sleep(self, creatures_list = creatures):
        if self.hunger == 0:
            # Die
            self.alive = False
        elif self.hunger == 1:
            # Survive
            pass
        elif self.hunger == 2:
            # Reproduce
            creatures_list.append(Creature())
                        
            
        
def init_creatures(creatures_list = creatures):
    creatures_list = [Creature()] * 12 # Creates 12 empty creatures

def init_food(food_list = food):
    food_list = [2] * 60 # Resets Food

def pick_all_food(creatures_list = creatures):
    for creature in creatures_list:
        if creature.alive:
            creature.pick_food()
    init_food()

def eat_all_food(food_list = food, creatures_list = creatures):
    # TODO: Add double detection
    for creature in creatures_list:
        if creature.alive:
            creature.eat_food()

    

def main():
    print("hello world")


if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()
