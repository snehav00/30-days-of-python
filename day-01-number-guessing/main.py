import random

print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.\nCan you guess it?")

play = 'y'
while play.lower() == 'y':
    number = random.randint(1, 100)
    attempt = 1
    while True:
        try:
            guess = int(input(f"guess #{attempt}: ")) 
            if guess < 1 or guess > 100:
                print("Out of range! Try again")
            elif guess == number:
                print("Correct!")
                print(f"You got it in {attempt} attempts.")
                break
            elif guess < number:
                print("Too low!")
                attempt += 1
            else:
                print("Too high!")
                attempt += 1
        except ValueError:
            print("This is not a valid integer.")
            
    play = input("Play again? (y/n): ")
print("Thanks for playing!")