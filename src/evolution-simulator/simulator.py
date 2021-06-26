import random
import time
from enum import Enum, auto
import plotter
from colorama import init, Fore

creatures = []
new_creatures = []  # * Creatures to be added after current ones have gone to sleep
foods = []  # * Food 'map'. Each item holds int food amount
score_table = {}  # * Should be written to in the format 'ROUND INDEX' : CREATURE COUNT

init()  # Initialize Colorama for coloured text in terminal


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
        self.hunger = foods[self.food_index].nutrition

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


class Food:
    def __init__(self, food_amount):
        # super(Food, self).__init__(food_amount) # dunno if this is needed?
        self.nutrition = food_amount


def consumption_handler(creature, food):
    creature.eat_food()
    food.nutrition -= creature.hunger


def reset_creatures(amount=12):
    global creatures
    for i in range(amount):
        creatures.append(Creature())  # Creates 12 empty creatures


def reset_food(amount=60):
    global foods
    foods = []
    for i in range(amount):
        foods.append(Food(2))  # Reset Food


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
            consumption_handler(creature, foods[creature.food_index])


def sleep_all(no_verbosity=False):
    if not no_verbosity:
        for creature in creatures:
            if creature.alive:
                state = creature.sleep()
                if state == State.SURVIVE:
                    print(
                        Fore.YELLOW + "Creature",
                        creatures.index(creature) + 1,
                        "survived.",
                    )
                elif state == State.REPRODUCE:
                    print(
                        Fore.GREEN + "Creature",
                        creatures.index(creature) + 1,
                        "reproduced.",
                    )
                elif state == State.DIE:
                    print(Fore.RED + "Creature", creatures.index(creature) + 1, "died.")
    else:
        for creature in creatures:
            if creature.alive:
                creature.sleep()
    creatures.extend(new_creatures)
    new_creatures.clear()


def print_food():
    print("\n\n")
    print(Fore.LIGHTMAGENTA_EX + "Food: ", end="")
    for food in foods:
        print(Fore.LIGHTGREEN_EX, end="") if food.nutrition > 0 else print(
            Fore.LIGHTBLACK_EX, end=""
        )
        print(food.nutrition, end="")
        time.sleep(0.1)


def print_creatures():
    print("\n\n")
    alive_creatures = [creature for creature in creatures if creature.alive]
    print(Fore.LIGHTMAGENTA_EX + "Number of creatures:", len(alive_creatures))
    print(Fore.LIGHTBLUE_EX + "\nCreature | Hunger")
    for creature in creatures:
        if creature.alive:
            print(Fore.GREEN, end="") if creature.hunger > 1 else print(
                Fore.LIGHTBLACK_EX, end=""
            )
            print(creatures.index(creature) + 1, creature.hunger)
            time.sleep(0.2)


def main_game_loop(days, creature_amount, food_amount, no_verbosity, *args):
    reset_creatures(creature_amount)
    score_counter(
        len([creature for creature in creatures if creature.alive]), 0
    )  # Day 0
    if not no_verbosity:
        for day in range(days):
            print(Fore.BLUE + "\n\n DAY", day + 1, "\n\n")
            reset_food(food_amount)
            print_food()
            None if args[0] > 0 else time.sleep(2)
            print_creatures()
            None if args[0] > 0 else time.sleep(5)
            pick_all_food()
            print("Food Picked")
            eat_all_food()
            None if args[0] > 0 else time.sleep(4)
            print("Food Eaten")
            print_creatures()
            None if args[0] > 0 else time.sleep(5)
            print_food()
            None if args[0] > 0 else time.sleep(4)
            print(Fore.YELLOW + "\nCreatures Reproduced, survived or died")
            sleep_all()
            None if args[0] > 0 else time.sleep(4)
            reset_hunger()
            None if args[0] > 1 else time.sleep(10)
            score_counter(
                len([creature for creature in creatures if creature.alive]), day + 1
            )  # Only select alive Creatures
    else:
        print(Fore.GREEN + "Simulating...")
        for day in range(days):
            reset_food(food_amount)
            pick_all_food()
            eat_all_food()
            sleep_all(True)
            reset_hunger()
            score_counter(
                len([creature for creature in creatures if creature.alive]), day + 1
            )
    score_writer() if not no_verbosity else None
    plot_score(days)


def score_writer():
    print(Fore.BLUE + "FINAL SCORE")
    score_keys = list(score_table.keys())
    score_vals = list(score_table.values())
    for score in score_table.values():
        print(
            score_keys[score_vals.index(score)] + 1, ":", score
        )  # Print score fancily


def score_counter(score, round):
    score_table[round] = score


def plot_score(days):
    score_keys = list(score_table.keys())
    score_vals = list(score_table.values())
    plotter.lineplot(
        score_keys,
        score_vals,
        "Days",
        "Population",
        "Creature-Food Simulation run for " + str(days) + " day(s).",
    )
