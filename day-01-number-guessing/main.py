import random

print("I'm thinking of a number between 1 and 100")
number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Enter your guess")) 
        if 1 > guess > 100:
            print("Out of range! Try again")
        elif guess == number:
            print("Correct!")
            breakpoint
        elif guess < number:
            print("Too low")
        else:
            print("Too high")
    except ValueError:
        print("This is not a valid integer.")