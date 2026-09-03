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
    
    computer_index = choices.index(computer_choice)
    user_index = choices.index(user_choice)
    
    if user_index > computer_index or (user_index == 0 and computer_index == 2):
        print("\nYou win!")
        user_wins += 1
    elif computer_index == user_index:
        print("\nTie")
        ties += 1
    else:
        print("\nComputer wins!")
        computer_wins += 1
    
    play_again = input("\nDo you want to play again?(y/n): ").lower()
    
print(f"Final scores\n\nYou: {user_wins}\nComputer: {computer_wins}\nTies: {ties}")

    
