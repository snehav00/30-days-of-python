import random

movies_quiz = [
    {
        "question": "In Notting Hill, what kind of shop does William own?",
        "choices": "Bookstore, Travel bookstore, Music store, Antique bookstore",
        "answer": "Travel bookstore"
    },
    {
        "question": "In 27 Dresses, what does Kevin initially do for a living?",
        "choices": "Writes about weddings, Works as a photographer, Runs a wedding venue, Works for a bridal magazine",
        "answer": "Writes about weddings"
    },
    {
        "question": "In The Proposal, what is Margaret Tate's position at the publishing company?",
        "choices": "Editor-in-chief, Senior editor, Executive assistant, Publishing director",
        "answer": "Senior editor"
    },
    {
        "question": "In How to Lose a Guy in 10 Days, what does Andie Anderson write about?",
        "choices": "Relationships and fashion, Lifestyle and relationships, Celebrity news, Travel and dating",
        "answer": "Lifestyle and relationships"
    },
    {
        "question": "In 10 Things I Hate About You, what instrument does Kat play?",
        "choices": "Guitar, Piano, Violin, Drums",
        "answer": "Guitar"
    } 
]

math_quiz = [
    {
        "question": "10*5-5*0+5",
        "choices": "50, 55, 45, 0",
        "answer": "55"
    },
    {
        "question": "11*11+9",
        "choices": "130, 139, 120, 129",
        "answer": "130"
    },
    {
        "question": "10+45/5",
        "choices": "10, 11, 15, 19",
        "answer": "19"
    },
    {
        "question": "4+2",
        "choices": "6, 4, 8, 10",
        "answer": "6"
    },
    {
        "question": "3*2+0+5",
        "choices": "14, 10, 15, 11",
        "answer": "11"
    }       
]


def game_choice():
    while True:
        print("Which quiz do you want to play?(Movies/Math)")
        quiz_choice = input().strip().lower()
        if quiz_choice == "movies" or quiz_choice == "movie":
            quiz_choice = movies_quiz
        elif quiz_choice == "math" or quiz_choice == "maths":
            quiz_choice = math_quiz
        else:
            print("Invalid choice! Choose movies or math\n")
            continue
        break
    return quiz_choice


def quiz(quiz_choice):
    score = 0
    random.shuffle(quiz_choice)
    print("=============\n|Python Quiz|\n=============")
    print("Choose the correct option")
    for i, ques in enumerate(quiz_choice):
        print(f"Question {i+1}: {ques['question']}")
        letters = "ABCD"
        for j, choice in enumerate(ques["choices"].split(", ")):
            print(f"{letters[j]}) {choice}")
            if choice == ques["answer"]:
                correct_option = letters[j]
            
        while True:
            user_answer = input("\nAnswer: ").strip().upper()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            print("\nInvalid option! Choose from A, B, C, D")
                        
        if user_answer == correct_option:
            print("CORRECT!\n")
            score += 1
        else: 
            print("WRONG!\n")
    print(f"Score: {score}/5")
        

def play():
    play_again = ""
    while play_again not in ['y', 'n']:
        play_again = input("Do you want to play again? Enter (y/n): ").strip().lower()
    if play_again == 'y':
        return True
    return False

game = game_choice()
quiz(game)
while play():
    quiz(game_choice())
