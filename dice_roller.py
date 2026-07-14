import random
from character import Character

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

def sgm_i():
    """ Created 12/07/2026
    All scores are recorded and arranged in the order the player desires. 4d6
    are rolled, and the lowest die (or one of the lower) is discarded. """
    num_stats = 6
    return [roll_four_drop_lowest() for _ in range(num_stats)]

def sgm_ii():
    """ Created 12/07/2026
    All scores are recorded and arranged as in Method I. 3d6 are rolled 12 times
    and the highest 6 scores are retained. """
    num_scores = 12
    highest_set = 6
    results = [roll_three() for _ in range(num_scores)]
    results.sort()
    return results[-highest_set:]

def sgm_iii(hero):
    """ Created 12/07/2026
    Scores rolled are according to each ability category, in order,
    Strength, Intelligence, Wisdom, Dexterity, Constitution, Charisma.
    3d6 are rolled 6 times for each ability, and the highest score is retained.
    """

    batch_size = 6

    hero.ability_scores = {
        ability: max(roll_three() for _ in range(batch_size))
        for ability in [
            "Strength",
            "Intelligence",
            "Wisdom",
            "Dexterity",
            "Constitution",
            "Charisma"
        ]
    }
    
def sgm_iv():
    """ Created 12/07/2026
    3d6 are rolled sufficient times to generate the 6 ability scores, in order,
    for 12 characters. The player then selects the single set of scores which he or she
    finds most desirable and these scores are noted on the character record sheet. """

    ability_order = ["Str","Int","Wis","Dex","Con","Cha"]
    batch_size = 12
    # Outer list comprehension generates 12 items: twelve 'characters'.
    # Inner dictionary comprehension rolls 2d6 for each ability in order
    
    return [{ability: roll_three() for ability in ability_order} for _ in range(batch_size)]

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
    
    # -------------------------------------------------------------------------
    # EXPLICIT INPUT CONFIGURATION MAP
    # -------------------------------------------------------------------------
    # Maps user-typed shorthand variations directly to the official dictionary keys.
    # All keys are forced to lowercase here to ensure case-insensitive lookups.
    input_translation_map = {
        "str": "Strength", "strength": "Strength",
        "int": "Intelligence", "intel": "Intelligence", "intelligence": "Intelligence",
        "wis": "Wisdom", "wisdom": "Wisdom",
        "dex": "Dexterity", "dexterity": "Dexterity",
        "con": "Constitution", "constitution": "Constitution",
        "cha": "Charisma", "char": "Charisma", "charisma": "Charisma"
    }

    while True:
        print("\nAvailable Abilities:")
        print("  " + ", ".join(unassigned_stats))
        
        # Capture user typing, strip leading/trailing whitespace, and make lowercase
        user_input = input("Type the target ability name or shortcut: ").strip().lower()
        
        # Check if the text matches any known translation entry
        if user_input not in input_translation_map:
            print(f"Error: '{user_input}' is not a recognised ability shortcut.")
            print(f"Please type something like: str, dex, con, or the full names.")
            continue
            
        # Extract the official name from our map
        resolved_ability_name = input_translation_map[user_input]
        
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
                stat_list = sgm_i()
                assign_rolled_stats(hero,stat_list)
                break
            case 2:
                stat_list = sgm_ii()
                assign_rolled_stats(hero,stat_list)
                break
            case 3:
                sgm_iii(hero)
                break
            case 4:
                print("That method hasn't been implemented yet.")
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
