print("==== TO-DO LIST ====\n")

all_tasks = []

def add_task(all_tasks):
    task = input("Enter task to add: ").strip()
    new_task = {"task": task, "done": False}
    all_tasks.append(new_task)

def display(all_tasks):
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
    
    

