print("==== TO-DO LIST ====\n")

all_tasks = []

def add_task(all_tasks):
    task = input("Enter task to add: ")
    new_task = {"task": task, "done": False}
    all_tasks.append(new_task)

def display(all_tasks):
    for i, item in enumerate(all_tasks):
        if item['done']:
            print(f"Task {i+1}: {item['task']} \u2713")
        else:    
            print(f"Task {i+1}: {item['task']}")

def delete_task(all_tasks):
    while True:
        try:
            task_number = int(input("\nEnter task number to delete: "))
            
            if task_number < 1 or task_number > len(all_tasks):
                print("Invalid task number!")
                continue
            break
        except ValueError:
            print("Invalid task number!")
    deleted = all_tasks.pop(task_number-1)
    print(f"'{deleted['task']}' removed\n")
    

add_task(all_tasks)
display(all_tasks)
delete_task(all_tasks)