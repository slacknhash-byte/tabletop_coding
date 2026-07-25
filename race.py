from constants import FIRST_EDITION_RACE_PREREQS

###
# Functions concerning player character race
# Created 25/07/2026

def check_prerequisites(hero, gender, race):
    """ Created 25/07/2026
    This function iterates through the ability scores set on the player
    character object and runs compare_stat on them.
    """
    
    for stat, value in hero.ability_scores.items():
        if value >= FIRST_EDITION_RACE_PREREQS[gender][race][stat]["minimum"] and value <= value >= FIRST_EDITION_RACE_PREREQS[gender][race][stat]["minimum"]:
            return True
        else:
            return False
