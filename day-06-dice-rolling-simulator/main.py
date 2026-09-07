import random

print("Dice rolling simulator\n")
def get_dice_number():
    while True:
        try:
            dice = int(input("Enter number of dice: "))
        except ValueError: 
            print("Invalid number!")
            continue
        if dice>0:
            return dice
        print("Number must be greater than 0\n")
    
def get_sides():
    while True:
        try:
            sides = int(input("Enter number of sides in a die: "))
        except ValueError: 
            print("Invalid number!")
            continue
        if sides>=2:
            return sides
        print("Number of sides must be atleast 2\n")

    
def roll_dice(dice, sides):
    rolls = []
    for i in range(dice):
        roll = random.randint(1, sides)
        rolls.append(roll)
    return rolls

def display(rolls):
    print("\nRolling\n")
    for i,roll in enumerate(rolls):
        print(f"Die {i+1}: {roll}")
    total = sum(rolls)
    print(f"\nTotal: {total}\n")

def ask_again():
    while True:
        another = input("Another round(y/n): ").strip().lower()
        if another in ['y', 'n']:
            return another
        print("Invalid choice! Enter 'Y' or 'N'.")

again = 'y'
while again == 'y':
    dice = get_dice_number()
    sides = get_sides()
    rolls = roll_dice(dice, sides)
    display(rolls)
    again = ask_again()

print("See you again!")
