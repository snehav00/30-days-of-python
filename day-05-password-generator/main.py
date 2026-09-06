import random 
import string

print("PASSWORD GENERATOR\n")

while True:
    try:
        length = int(input("\nEnter password length(8 to 64): "))
    except ValueError:
        print("Enter valid length")
        continue
    if length>=8 and length<=64:
        break
    print("Password length must be between 8 and 64. ")

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
special = string.punctuation

all_chars = uppercase+lowercase+numbers+special




