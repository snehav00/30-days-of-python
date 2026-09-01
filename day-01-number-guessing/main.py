import random

print("I'm thinking of a number between 1 and 100")
number = random.randint(1, 100)
attempt = 0;
while True:
    try:
        attempt += 1
        guess = int(input(f"guess #{attempt}: ")) 
        if 1 > guess > 100:
            print("Out of range! Try again")
        elif guess == number:
            print("Correct!")
            print(f"You got it in {attempt} attempts.")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
    except ValueError:
        print("This is not a valid integer.")