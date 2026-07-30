""" biographical.py
Created 28/07/2026

This file contains functions used for setting biographical details
of the character object. Most of these are cosmetic (height, weight, hair, eyes)
although some can have a game-mechanical application (age), or even affect
Strength score and level limits (gender in 1st edition AD&D).
"""

from character import Character
from constants import AFFIRMATIVES
from constants import NEGATIVES
from constants import MASCULINE_ABBREVIATION_LIST
from constants import FEMININE_ABBREVIATION_LIST

""" Created 28/07/2026
1st Edition AD&D limits Strength scores for demihuman characters. Users have
the option to waive this rule.
"""

def check_1E_gender_rule(hero):
    print("This is a 1st Edition AD&D character. Female characters in this edition")
    print("have limitations on their Strength score, which in turn results in lower")
    print("level limits for female nonhuman fighters. This rule did not survive into")
    print("later editions.")
    ignore_limit = input("Do you wish to ignore this rule? (default: Yes) ")
    hero.ignore_1e_gender_rule = False if ignore_limit in NEGATIVES else True



def get_character_sex(hero):
    """ Created 28/07/2026
    Last modified 30/07/2026
    This function prompts the user for their character's biological sex.
    """
    print("Which sex was your character assigned at birth?")
    print("\t1) Male\n\t2) Female\n\tOther (please specify)\n")
    input_sex = input("Your character's sex: ")
    match input_sex:
        case "1":
            sex = "male"
        case "2":
            sex = "female"
        case _:
            sex = input_sex
    hero.biography["sex"] = sex
        
""" Created 28/07/2026
This function prompts the user for their character's gender.
"""
            
def get_gender(hero):
    while True:
        gender = input("")
