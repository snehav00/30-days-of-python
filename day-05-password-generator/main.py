import random 
import string

print("PASSWORD GENERATOR\n")

def take_length():
    while True:
        try:
            length = int(input("\nEnter password length(8 to 64): "))
        except ValueError:
            print("Enter valid length")
            continue
        if 8 <= length <= 64:
            return length
        print("Password length must be between 8 and 64. ")

def generate(length):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special = string.punctuation

    all_chars = uppercase+lowercase+numbers+special
    
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(numbers),
        random.choice(special)
    ]
    while len(password)<length: 
        password.append(random.choice(all_chars))
    random.shuffle(password)
    password = ''.join(password)
    return password

def display(password):
    print(f"\nGenerated Password: {password}")
    
def strength(length):
    if length<12:
        print("\nStrength: Medium")
    elif length<=15:
        print("\nStrength: Strong")
    else:
        print("\nStrength: Very strong")
        
    
def make_another():
    while True:
        again = input("\nDo you want to generate another password?(y/n)").strip().lower()
        if again in ['y', 'n']:
            return again
        else:
            print("Invalid choice")
            

again = 'y'
while again == 'y':
    length = take_length()
    password = generate(length)
    display(password)
    strength(length)
    again = make_another()

print("\nThanks for using our service!")
