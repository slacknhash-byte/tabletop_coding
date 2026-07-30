from constants import FIRST_EDITION_RACE_PREREQS
from constants import FIRST_EDITION_RACE_LIST

###
# Functions concerning player character race
# Created 25/07/2026

def check_prerequisites(hero, sex, race):
    """ Created 25/07/2026
    This function iterates through the ability scores set on the player
    character object and runs compare_stat on them.
    """
    
    for stat, value in hero.ability_scores.items():
        if value >= FIRST_EDITION_RACE_PREREQS[sex][race][stat]["minimum"] and value <= value >= FIRST_EDITION_RACE_PREREQS[sex][race][stat]["minimum"]:
            return True
        else:
            return False

def build_1e_race_list(hero):
    """ Created 30/07/2026
    This function runs check_prerequisites() on each of the players
    character races. If the character qualifies (check_prerequisites returns
    True) then the name of that race is added to the list of races for
    which they qualify. The function returns that list.
    """
    race_list = []
    sex = "female" if hero.biography["sex"] == "female" and hero.ignore_1e_gender_rule == False else "male"
    for race_name in FIRST_EDITION_RACE_LIST:
        if check_prerequisites(hero, sex, race_name) == True:
            race_list.append(race_name)
    return race_list   

def output_race_list(race_list):
    """ Created 30/07/2026
    This funnction takes a list (usually generated from build_1e_race_list())
    and outputs it as a string, delimited by commas.
    """
    print("Your stats qualify you for the following races:")
    print(f"{', '.join(race_list)}")

def get_race(race_list):
    """ Created 30/07/2026
    This function prompts the user to enter the race for their character.
    If the race is not on the list, then the choice is rejected and the user
    informed as such. Otherwise, the function returns a string containing
    the chosen race.
    """

    while True:
        choice = input("Which race do you wish your character to be? ")
        if choice.lower() in race_list:
            race = choice.lower()
            print(f"You have chosen: {race}")
            return race
        else:
            print("Sorry! That isn't a valid option.")
            output_race_list(race_list)
