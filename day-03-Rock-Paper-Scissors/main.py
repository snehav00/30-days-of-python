print("Welcome to Rock Paper Scissors!")

play_again = 'y'
choices = ["rock", "paper", "scissors"]

while play_again == 'y':  
    user_choice = input("Your choice: ").lower()
    if user_choice not in choices:
        print("Invalid input! Choose rock, paper or scissors")
        continue
    
    
