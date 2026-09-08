# Day 7 — To-Do List 📝

This program allows users to create, view, complete, and delete tasks through a simple interactive menu.

## Features

- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Display completed tasks with a ✓
- Handle invalid user input
- Handle an empty task list

## Technologies Used

- Python 3

## Concepts Practiced

- Functions
- Lists
- Dictionaries
- `while` loops
- `for` loops
- `if/else`
- `match/case`
- List indexing
- `enumerate()`
- `append()`
- `pop()`
- `len()`
- Boolean values
- Input validation
- `try/except`
- Returning values from functions

## Data Structure

Each task is stored as a dictionary:

```python
all_tasks = [{
    "task": "Study Python",
    "done": False
}]

```

## Example

```text
==== TO-DO LIST ====

1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit

Choose an option 1 to 5: 1

Enter task to add: Study Python

Current Status:
Task 1: Study Python

Choose an option 1 to 5: 3

Task number: 1
Task 'Study Python' marked as completed

Current Status:
Task 1: Study Python ✓

Choose an option 1 to 5: 4

Task number: 1
'Study Python' removed

No tasks yet.

Choose an option 1 to 5: 5

Goodbye!
```

## What I learned

This project introduced me to working with structured data using lists and dictionaries.

I also practiced separating different responsibilities into functions and learned how to modify and remove items from a list.

A key concept I practiced was CRUD:

- Create → Add a task
- Read → View tasks
- Update → Complete a task
- Delete → Delete a task


## Future Improvements

- Edit existing tasks
- Add task priorities
- Add due dates
- Search for tasks
- Save tasks to a JSON file
- Load tasks when the program starts
- Clear all completed tasks