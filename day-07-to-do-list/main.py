print("==== TO-DO LIST ====\n")

all_tasks = []

def add_task(all_tasks):
    while True:
        task = input("Enter task to add: ")
        if task:
            new_task = {"task": task, "done": False}
            all_tasks.append(new_task)
            break
        print("Task cannot be empty")

def display(all_tasks):
    if not all_tasks:
        print("No tasks yet.\n")
        return
    print("\nCurrent Status:")
    for i, item in enumerate(all_tasks):
        if item['done']:
            print(f"Task {i+1}: {item['task']} \u2713")
        else:    
            print(f"Task {i+1}: {item['task']}")

def ask_task_number(length):
    while True:
        try:
            task_number = int(input("\nTask number: "))
            
            if task_number >= 1 and task_number <= length:
                return task_number
            print("Invalid task number!\n")
        except ValueError:
            print("Invalid task number!\n")

def delete_task(all_tasks):
    task_number = ask_task_number(len(all_tasks))
    deleted = all_tasks.pop(task_number-1)
    print(f"'{deleted['task']}' removed\n")
    
def complete_task(all_tasks):
    task_number = ask_task_number(len(all_tasks))
    task = all_tasks[task_number-1]
    if not task['done']:
        task['done'] = True
        print(f"Task '{task['task']}' marked as completed")
    else:
        print(f"Task '{task['task']}' is already completed!")

def menu(all_tasks):
    while True:
        print("\n1. Add task\n2. View tasks\n3. Complete task\n4. Delete task\n5. Exit\n")
        try:
            user_choice = int(input("\nChoose an option 1 to 5: "))
            match user_choice:
                case 1:
                    add_task(all_tasks)
                    display(all_tasks)
                case 2:
                    display(all_tasks)
                case 3:
                    complete_task(all_tasks)
                    display(all_tasks)
                case 4:
                    delete_task(all_tasks)
                    display(all_tasks)
                case 5:
                    return
                case _:
                    print("Invalid number choice!\n")
        except ValueError:
            print("Not a number!\n")
            
menu(all_tasks)
print("Goodbye!")
