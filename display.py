"""
Created 27/07/2026
Last modified 30/07/2026 
"""
def display_character_sheet(hero):
    """ Created 14/07/2026
    28/07/2026: Added ignore gender rule.
    30/07/2026: Added sex and race.
    After the generation method has been chosen and the stats are assigned, we should
    see the character sheet.
    """
    output_horizontal_rule()
    print(f"{hero.name}")
    print(f"Race: {hero.char_race.capitalize()}")
    output_horizontal_rule()
    print(f"Sex: {hero.biography["sex"].capitalize()}")
    
    if hero.ignore_1e_gender_rule != False:
        print("Ignoring 1st Edition AD&D gender rule.")
    else:
        print("Following 1st Edition AD&D gender rule.")
    output_horizontal_rule()
    for stat, value in hero.ability_scores.items():
        print(f"  {stat.capitalize()}: {value}")
    output_horizontal_rule()

def output_horizontal_rule():
    """ Created 14/07/2026
    Outputs a simple horizontal ruling line to break text up.
    """
    print("\n========================================")
