import random

def prompt_for_dice():   
    number_of_dice = int(input("How many dice do you wish to roll? "))
    number_of_sides = int(input("How many sides per die? "))
    dice_rolled = [random.randint(1,number_of_sides) for _ in range(number_of_dice)]                      
    print("You rolled:", ', '.join(str(roll) for roll in dice_rolled))
    print("Total:",sum(dice_rolled))

def stat_roll():
    """ The traditional way to generate a D&D ability score is to
    roll 4d6, drop the lowest, and take the total of the rest. """

    num_dice = 4
    num_sides = 6
    rolls = [random.randint(1,num_sides) for _ in range(num_dice)]
    print("You rolled:", ', '.join(str(roll) for roll in rolls))
    print("Total:",sum(rolls)-min(rolls))
    return sum(rolls)-min(rolls)
    
def main():
    print("Generating stats: ")
    stat_list = [stat_roll() for _ in range(6)]
    print("You rolled: ",', '.join(str(roll) for roll in stat_list))
    
if __name__ == "__main__":
    main()
