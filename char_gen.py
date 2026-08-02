from character import Character
from constants import FIRST_EDITION_RACES
from stat_generation_methods import generation_method_menu
from race import check_prerequisites
from display import display_character_sheet
from display import output_horizontal_rule
from biographical import get_character_sex
from biographical import check_1E_gender_rule
from race import build_1e_race_list
from race import output_race_list
from race import get_race

def main():
    """
    25/07/2026: Moved to char_gen.py
    30/07/2026: Added function calls to set sex and race.
    """
    hero_name = input("Enter a name for your character: ")
    hero = Character(name=hero_name)
    generation_method_menu(hero)
    check_1E_gender_rule(hero)    
    get_character_sex(hero)
    race_list = build_1e_race_list(hero)
    output_race_list(race_list)
    hero.char_race = get_race(race_list)
    
    display_character_sheet(hero)
    
if __name__ == "__main__":
    main()

