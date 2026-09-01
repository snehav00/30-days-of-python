# Day 1 — Number Guessing Game 🎯

A simple command-line number guessing game built with Python.

The computer randomly chooses a number between 1 and 100, and the player keeps guessing until they find the correct number.

## Features

* Generates a random number between 1 and 100
* Gives hints when the guess is too high or too low
* Tracks the number of attempts
* Handles invalid inputs
* Prevents guesses outside the 1–100 range
* Allows the player to start a new game
* Supports uppercase and lowercase `Y` for replaying

## Concepts Practiced

* Variables
* User input with `input()`
* Type conversion with `int()`
* Conditional statements (`if`, `elif`, `else`)
* `while` loops
* `try` / `except` error handling
* The `random` module
* Comparison operators
* Formatted strings (f-strings)

## How to Run

Make sure Python is installed on your computer.

Navigate to the project folder and run:

```bash
python main.py
```

## Example

```text
Welcome to the number guessing game!
I'm thinking of a number between 1 and 100.
Can you guess it?

guess #1: 50
Too low!

guess #2: 75
Too high!

guess #3: 63
Correct!
You got it in 3 attempts.

Play again? (y/n): n
Thanks for playing!
```

## What I Learned

While building this project, I practiced controlling program flow with loops and conditional statements. I also learned how to handle invalid user input using `try` and `except`, generate random numbers, and keep track of attempts during a game.

## Future Improvements

* Add difficulty levels
* Add a maximum number of attempts
* Add a scoring system
* Keep track of the best score
* Add more input validation for the replay option
