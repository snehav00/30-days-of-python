# 🧮 Day 2 — Python Calculator

A command-line calculator built with Python as part of my **30 Days of Python** challenge.

The goal of this project was to practice functions, conditional logic, loops, user input, and error handling while building something functional.

## ✨ Features

* Addition `+`
* Subtraction `-`
* Multiplication `*`
* Division `/`
* Modulus `%`
* Decimal number support
* Invalid operator handling
* Invalid number handling
* Division-by-zero handling
* Exit option
* Reuse the previous result in the next calculation
* Continuous calculations using a loop

## 🧠 Concepts Practiced

* Variables
* `input()`
* Type conversion with `float()`
* Functions
* `match` / `case`
* `while` loops
* `if` statements
* `continue`
* `try` / `except`
* Exception handling
* `None`
* Basic arithmetic operators

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

## 💻 Example

```text
=====================
  PYTHON CALCULATOR
=====================

Enter first number: 10
Enter operator(+, -, *, /, %): +
Enter second number: 5

Result: 15
```

The calculator can also reuse the previous result:

```text
Result: 15

Do you want to use 15.0 further (y/n): y

Enter operator(+, -, *, /, %): *
Enter second number: 2

Result: 30
```

## 📚 What I Learned

* How to create and use functions in Python.
* How `match` / `case` can be used when checking different possible values.
* How `while` loops can keep a program running until a condition is met.
* How `continue` can skip the current loop iteration and start the next one.
* How `try` / `except` can prevent certain errors from crashing the program.
* How Python returns `None` when a function doesn't explicitly return a value.

## 🧩 Challenges I Faced

One challenge was handling invalid operators without terminating the calculator.

I solved this by checking whether the calculation returned `None` and using `continue` to restart the loop.

## 🚀 Future Improvements

* Add calculation history
* Add more mathematical operations
* Improve input validation
* Allow the user to enter expressions such as `10 + 5 * 2`
* Build a GUI version

---
