# Day 6 — Dice Rolling Simulator 🎲

A command-line dice rolling simulator built with Python as part of my **30 Days of Python** challenge.

The program allows the user to choose how many dice to roll and how many sides each die should have. It then generates random results and displays the individual rolls and their total.

## Features

- Choose the number of dice to roll
- Choose the number of sides for each die
- Randomly generate each dice roll
- Display individual dice results
- Calculate and display the total
- Validate user input
- Roll again without restarting the program

## Technologies Used

- Python 3
- `random` module

## Concepts Practiced

- Functions
- `while` loops
- `for` loops
- Lists
- Input validation
- `try` / `except`
- `random.randint()`
- `enumerate()`
- `sum()`
- Returning values from functions

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```
## Example
```text
Dice rolling simulator

Enter number of dice: 4
Enter number of sides in a die: 6

Rolling

Die 1: 4
Die 2: 6
Die 3: 2
Die 4: 5

Total: 17

Another round(y/n): n
See you again!
```

## What I learned

This project helped me practice using for loops to repeat an operation multiple times and storing the results in a list.

I also learned how Python's built-in sum() function can be used to calculate the total of values in a list.

The project also gave me more practice with functions, input validation, exception handling, and random number generation.

## Future Improvements

- Track statistics across multiple rounds
- Add different types of dice