# Day 3 — Rock Paper Scissors 🪨📄✂️

A command-line Rock Paper Scissors game built with Python as part of my **30 Days of Python** learning challenge.

The player competes against the computer, which randomly selects Rock, Paper, or Scissors. The game validates user input, determines the winner, tracks scores, and allows multiple rounds to be played.

## Features

- Player vs. computer gameplay
- Random computer selection
- Case-insensitive input
- Automatic whitespace handling
- Input validation
- Replay functionality
- Replay input validation
- Score tracking
- Final score summary
- Handles wins, losses, and ties

## Game Rules

| Player | Computer | Result |
|--------|----------|--------|
| Rock | Scissors | Player wins |
| Paper | Rock | Player wins |
| Scissors | Paper | Player wins |
| Same choice | Same choice | Tie |
| All other combinations | | Computer wins |

## Technologies Used

- Python 3
- `random` module

## Concepts Practiced

- Variables and assignment
- Lists
- User input with `input()`
- String methods: `.strip()` and `.lower()`
- Conditional statements
- `while` loops
- `continue`
- Logical operators (`and`, `or`)
- Membership operators (`in`, `not in`)
- `random.choice()`
- Counters
- Basic game logic
- Input validation

## How to Run

### Prerequisites

Make sure Python 3 is installed on your system.

### Run the Game

Clone the repository and navigate to the project directory:

```bash
git clone <https://github.com/snehav00/30-days-of-python.git>
cd 30-days-of-python/day-03-Rock-Paper-Scissors
```
### Run the program

```bash
python main.py
```

## Example
```text
Welcome to Rock Paper Scissors!

Your choice: rock
Computer choice: scissors

You win!

Do you want to play again? (y/n): y

Your choice: paper
Computer choice: scissors

Computer wins!

Do you want to play again? (y/n): n

|Final scores|

You: 1
Computer: 1
Ties: 0
```
## What I Learned

This project helped me strengthen my understanding of:

- Using `while` loops to control program flow
- Using `if`, `elif`, and `else` for decision-making
- Working with lists and `random.choice()`
- Taking and validating user input
- Using `.strip()` and `.lower()` to handle user input
- Using `and` and `or` to build logical conditions
- Tracking values with counters
- Managing game state across multiple rounds
- Refactoring code to make the logic clearer and easier to maintain

I also learned that writing simple and readable logic is often better than making the code unnecessarily complicated.

## Future Improvements

- Refactor the game using functions
- Use a dictionary to represent the game rules
- Add best-of-3, best-of-5, and custom match modes
- Add round history
- Improve the command-line interface
- Add more input shortcuts such as `r`, `p`, and `s`