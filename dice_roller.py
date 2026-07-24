import random
from character import Character
from constants import ABILITY_NAMES
from constants import INPUT_TRANSLATION_MAP
from constants import ABBREVIATION_MAP
from constants import ABILITY_NAMES

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

# SGMs, or Stat Generation Methods. The Dungeron Masters Guide calls those four
# ways to roll up a character 'methods'. I've named them 'SGMs' in order to reduce
# confusion with the programming term 'method'.

def edition_1_sgm_i():
    """ Created 12/07/2026
    All scores are recorded and arranged in the order the player desires. 4d6
    are rolled, and the lowest die (or one of the lower) is discarded. """
    num_stats = 6
    return [roll_four_drop_lowest() for _ in range(num_stats)]

def edition_1_sgm_ii():
    """ Created 12/07/2026
    All scores are recorded and arranged as in Method I. 3d6 are rolled 12 times
    and the highest 6 scores are retained. """
    num_scores = 12
    highest_set = 6
    results = [roll_three() for _ in range(num_scores)]
    results.sort()
    return results[-highest_set:]

def edition_1_sgm_iii(hero):
    """ Created 12/07/2026
    Scores rolled are according to each ability category, in order,
    Strength, Intelligence, Wisdom, Dexterity, Constitution, Charisma.
    3d6 are rolled 6 times for each ability, and the highest score is retained.
    """

    batch_size = 6

    hero.ability_scores = {
        ability: max(roll_three() for _ in range(batch_size))
            for ability in ABILITY_NAMES
    }
    
def edition_1_sgm_iv():
    """ Created 12/07/2026
    3d6 are rolled sufficient times to generate the 6 ability scores, in order,
    for 12 characters. The player then selects the single set of scores which he or she
    finds most desirable and these scores are noted on the character record sheet. """

    ability_order = ABILITY_NAMES
    batch_size = 12
    # Outer list comprehension generates 12 items: twelve 'characters'.
    # Inner dictionary comprehension rolls 3d6 for each ability in order
    
    return [{ability: roll_three() for ability in ability_order} for _ in range(batch_size)]

###
# Functions to assist with character generation method IV
def output_stat_sets(stat_list):
    """ Created 24/07/2026
    Outputs the contents of stat_list, which is a two-dimensional list.
    In pretty much every case, stat_list consists of multiple sets of stats
    (typically twelve sets of character ability scores as per method I in
    the 1st Edition AD&D Dungeon Masters Guide).
    """
    print("The following ability scores have been generated:\n")
    for number, stat_set in enumerate(stat_list, start=1):
        line = ", ".join(
            f"{ability} {score:2}"
            for ability, score in stat_set.items()
        )
        print(f"{number:2}. {line}")

def select_stat_set(set_size):
    """ Created 24/07/2026
    Prompts the user to pick a number between 1 and set_size, and rejects
    all other inputs.
    """
    while True:
        try:
            choice = int(input(f"Pick a number between 1 and {set_size}: "))
            if choice in range(1,set_size+1):
                return choice
            else:
                print(f"Please pick a number between 1 and {set_size}.")
        except ValueError:
            print(f"That is not a number. Please pick a number between 1 and {set_size}.")

def assign_stat_set(hero, choice, stat_list):
    """ Created 24/07/2026
    This function takes choice, subtracts 1 in otder to get the array index corresponding
    to the user's choice, and applies the contents of stat_list[choice] to the hero object.
    """
    index = choice - 1
    hero.ability_scores = stat_list[index]
    
###
    
def output_horizontal_rule():
    """ Created 14/07/2026
    Outputs a simple horizontal ruling line to break text up.
    """
    print("\n========================================")

def display_assignment_menu(local_scores, stat_list, assigned_list, unassigned_stats):
    """ Created 13/07/2026
    Modified 14/07/2026
    Prints the current status of the character sheet and open rolls."""
    output_horizontal_rule()
    print("--- CURRENT CHARACTER SHEET ---")
    for stat, value in local_scores.items():
        print(f"  {stat}: {value}")
        
    print("\n--- AVAILABLE ROLLS ---")
    available_rolls = [
        str(score) for index, score in enumerate(stat_list) 
        if assigned_list[index] == 0
    ]
    print("  " + ", ".join(available_rolls))
    output_horizontal_rule()


def get_valid_score_index(stat_list, assigned_list) -> int:
    """ Created 13/07/2026
    Prompts for a score and returns its verified index in stat_list."""
    while True:
        try:
            score_choice = int(input("\nEnter the value you want to assign: "))
        except ValueError:
            print("Error: Please enter a valid whole number.")
            continue
            
        # Locate the first available matching index
        target_index = -1
        for index, score in enumerate(stat_list):
            if score == score_choice and assigned_list[index] == 0:
                target_index = index
                break 
                
        if target_index == -1:
            print(f"Error: {score_choice} is not available! Check the list.")
            continue
            
        return target_index


def get_valid_ability(local_scores, unassigned_stats) -> str:
    """ Created 13/07/2026
    Prompts for an ability name, normalises variations, and validates choices."""   

    while True:
        print("\nAvailable Abilities:")
        print("  " + ", ".join(unassigned_stats))
        
        # Capture user typing, strip leading/trailing whitespace, and make lowercase
        user_input = input("Type the target ability name or shortcut: ").strip().lower()
        
        # Check if the text matches any known translation entry
        if user_input not in INPUT_TRANSLATION_MAP:
            print(f"Error: '{user_input}' is not a recognised ability shortcut.")
            print(f"Please type something like: str, dex, con, or the full names.")
            continue
            
        # Extract the official name from our map
        resolved_ability_name = INPUT_TRANSLATION_MAP[user_input]
        
        # Now perform validation checks using the clean, explicit full name
        if resolved_ability_name not in unassigned_stats:
            print(f"Error: {resolved_ability_name} already has a score assigned!")
            print(f"Remaining choices left: {', '.join(unassigned_stats)}")
            continue
            
        # Return the verified, clean full string to the orchestrator
        return resolved_ability_name

def assign_rolled_stats(character_object, stat_list):
    """
    Created 13/07/2026
    Main Orchestrator: Coordinates the sub-functions locally and 
    commits the results to the character object at the end.
    """
    # 1. Initialize Local Workspace States
    stat_list.sort()
    ability_names = list(character_object.ability_scores.keys())
    local_scores = {ability: "Unassigned" for ability in ability_names}
    
    assigned_list = [0] * len(stat_list)
    unassigned_stats = list(ability_names)

    # 2. Main Control Loop (Delegating to Helpers)
    while len(unassigned_stats) > 0:
        display_assignment_menu(local_scores, stat_list, assigned_list, unassigned_stats)
        
        # Get verified index and verified ability name
        target_index = get_valid_score_index(stat_list, assigned_list)
        ability_choice = get_valid_ability(local_scores, unassigned_stats)
        
        # Update local states
        local_scores[ability_choice] = stat_list[target_index]
        assigned_list[target_index] = 1
        unassigned_stats.remove(ability_choice)
        
        print(f"\n-> Success! Locally staged {stat_list[target_index]} to {ability_choice}.")

    # 3. Final Commit Transaction
    character_object.ability_scores = local_scores
    print("\nCharacter Generation Complete! Changes saved to character record.")

def display_character_sheet(hero):
    """ Created 14/07/2026
    After the generation method has been chosen and the stats are assigned, we should
    see the character sheet.
    """
    output_horizontal_rule()
    print(f"{hero.name}")
    for stat, value in hero.ability_scores.items():
        print(f"  {stat}: {value}")
    output_horizontal_rule()

def output_menu_options():
    """ Created 13/07/2026
    Modified 14/07/2026
    This function presents the character generation options to the user.
    """
    output_horizontal_rule()
    print("There are four methods to generate your ability scores:")
    print("\t1: Roll 4d6, drop the lowest. Repeat six times and assign the scores according to your choice.")
    print("\t2: Roll 3d6. Repeat twelve times times and assign the top six highest scores according to your choice.")
    print("\t3: Roll 3d6 six times each for Strength, Intelligence, Wisdom, Dexterity, Constitution, and Charisma in that order. Pick the highest score for each ability score.")
    print("\t4: Roll 3d6 in order for Strength, Intelligence, Wisdom, Dexterity, Constitution, and Charisma. Repeat twelve times and pick one set.")
    output_horizontal_rule()
    

def generation_method_menu(hero):
    """ Created 13/07/2026
    The Dungeon Masters Guide offers four ways to generate a character. Let's
    presume the program offers you a choice. """
    output_menu_options()
    while True:
        menu_choice=int(input("\nHow do you want to generate your character? "))
        match menu_choice:
            case 1:
                stat_list = edition_1_sgm_i()
                assign_rolled_stats(hero,stat_list)
                break
            case 2:
                stat_list = edition_1_sgm_ii()
                assign_rolled_stats(hero,stat_list)
                break
            case 3:
                edition_1_sgm_iii(hero)
                break
            case 4:
                rolled_stats = edition_1_sgm_iv()
                output_stat_sets(rolled_stats)
                chosen_set = select_stat_set(len(rolled_stats))
                assign_stat_set(hero, chosen_set, rolled_stats)
                break
            case _:
                print("Please pick an option between 1 and 4.")
        
    
def main():
    #pick_generation_method()
    hero_name = input("Enter a name for your character: ")
    hero = Character(name=hero_name)
    generation_method_menu(hero)
    display_character_sheet(hero)
    
if __name__ == "__main__":
    main()
