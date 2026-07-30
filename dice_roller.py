import random
from character import Character
from constants import ABILITY_NAMES
from constants import INPUT_TRANSLATION_MAP
from constants import ABBREVIATION_MAP
from constants import ABILITY_NAMES
from constants import ABILITY_SHORT_NAMES
from display import output_horizontal_rule
from display import display_character_sheet


###
# Dice-rolling functions

def die(num_sides):
    """ Created 12/07/2026
        Rolls a single die of a variable number of sides """
    return random.randint(1,num_sides)

def d6():
    """ Created 12/07/2026
        Rolls a single six-sided die """
    return random.randint(1,6)

def prompt_for_dice():   
    number_of_dice = int(input("How many dice do you wish to roll? "))
    number_of_sides = int(input("How many sides per die? "))
    dice_rolled = [random.randint(1,number_of_sides) for _ in range(number_of_dice)]                      
    print("You rolled:", ', '.join(str(roll) for roll in dice_rolled))
    print("Total:",sum(dice_rolled))

def roll_four_drop_lowest():
    """ 4d6 are rolled, and the lowest die (or one of the lower) is discarded. """

    num_dice = 4
    num_sides = 6
    rolls = [die(num_sides) for _ in range(num_dice)]
    return sum(rolls)-min(rolls)

def roll_three():
    """ Rolls three six-sided dice, returns total """
    num_sides = 6
    num_dice = 3
    return sum([die(num_sides) for _ in range(num_dice)])


        
    
