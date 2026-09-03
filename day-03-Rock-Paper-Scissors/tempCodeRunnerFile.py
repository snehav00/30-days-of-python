import random

print("Welcome to Rock Paper Scissors!")

play_again = 'y'
choices = ["rock", "paper", "scissors"]
user_wins = computer_wins = ties = 0
while play_again == 'y':  
    user_choice = input("\nYour choice: ").strip().lower()
    if user_choice not in choices:
        print("Invalid input! Choose rock, paper or scissors")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer choice: {computer_choice}")
    
    if (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("\nYou win!")
        user_wins += 1
    elif user_choice == computer_choice:
        print("\nTie")
        ties += 1
    else:
        print("\nComputer wins!")
        computer_wins += 1
    
    play_again = input("\nDo you want to play again?(y/n): ").strip().lower()
    while play_again not in ['y', 'n']:
        print("Invalid input! Enter 'y' or 'n'")
        play_again = input("\nDo you want to play again?(y/n): ").strip().lower()
    
print(f"\n|Final scores|\n\nYou: {user_wins}\nComputer: {computer_wins}\nTies: {ties}\n")

    
