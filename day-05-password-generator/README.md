# Day 5 — Password Generator 🔐

A command-line Password Generator built with Python as part of my **30 Days of Python** challenge.

This application generates secure random passwords while guaranteeing at least one uppercase letter, one lowercase letter, one digit, and one special character.

## Features

- Generate passwords between **8–64** characters
- Guarantees character variety
- Randomized password order using `shuffle()`
- Input validation
- Generate multiple passwords in one session
- Modular design using functions

## Technologies Used

- Python 3
- `random`
- `string`

## Concepts Practiced

- Functions
- Loops
- Lists
- String manipulation
- Random number generation
- Input validation
- Exception handling (`try` / `except`)
- List operations
- `random.shuffle()`

## How to Run

```bash
python main.py
```

## Example

```text
PASSWORD GENERATOR

Enter password length (8 to 64): 12

Generated Password:
A@7kP!2xLm9#

Do you want to generate another password? (y/n): n

Thanks for using our service!
```

## What I Learned

This project helped me understand how to organize code into reusable functions, validate user input with exception handling, and generate secure random data using Python's `random` and `string` modules.

## Future Improvements

- Let users choose whether to include numbers or symbols
- Copy password to clipboard automatically
- Save generated passwords to a file
- Create a graphical user interface (GUI)

---
