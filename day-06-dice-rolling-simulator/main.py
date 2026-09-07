import random

print("Dice rolling simulator\n")
def dice_number():
    try:
        dice = int(input("Enter number of dice: "))
    except ValueError: 
        print("Invalid number!")
    return dice
    
def sides():
    try:
        sides = int(input("Enter number of sides in a die: "))
    except ValueError: 
            print("Invalid number!")
    return sides
    
def roll_dice(dice, sides):
    rolls = []
    for i in range(dice):
        roll = random.randint(1, sides)
        rolls.append(roll)
    return rolls;

def display(rolls):
    print("\nRolling\n")
    sum = 0
    for i,roll in enumerate(rolls):
        print(f"Die {i+1}: {roll}")
        sum += roll
    print(f"\nTotal: {sum}\n")


dice = dice_number()
sides = sides()
rolls = roll_dice(dice, sides)
display(rolls)